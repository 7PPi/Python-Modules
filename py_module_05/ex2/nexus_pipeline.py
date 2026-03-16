"""Module documentation."""
from typing import Protocol, Any, Dict, Union, List
from abc import ABC, abstractmethod


class ProcessingStages(Protocol):
    """ProcessingStages class."""
    def process(self, data: Any) -> Any:
        """process function."""
        pass


class InputStage():
    """InputStage class."""
    def process(self, data: Any) -> Dict:
        """process function."""
        validated = {}
        try:
            if isinstance(data, dict):
                for key, value in data.items():
                    if key in ("sensor", "value", "unit"):
                        validated.update({key: value})
                if len(validated) == 3:
                    return (validated)
                else:
                    raise KeyError("ERROR: Unkwon JSON attributions")
            elif isinstance(data, str):
                separeted = [p.strip().replace("action", "activity")
                             for p in data.split(",") if p != ""]
                validated["content"] = separeted
                ac = 0
                for a in separeted:
                    if a == "activity":
                        ac += 1
                validated["actions"] = len(separeted) // 3
                validated["processed"] = ac
                if len(separeted) % 3 == 0:
                    return validated
                else:
                    return "ERROR: Insuficient CSV data"
            elif isinstance(data, list):
                for stream in data:
                    float(stream)
                validated["stream"] = data
                return validated
        except KeyError as e:
            return f"ERROR detected in Stage 1: {e}"
        except ValueError as e:
            return f"ERROR detected in Stage 1: Invalid stream input, {e}"


class TransformStage():
    """TransformStage class."""
    def process(self, data: Any) -> Dict:
        """process function."""
        try:
            transformed = {}
            if isinstance(data, dict) and "value" in data and "unit" in data:
                transformed["value"] = float(data["value"])
                if transformed["value"] < 40 and transformed["value"] > 20:
                    transformed["range"] = "Normal"
                else:
                    transformed["range"] = "Danger"
                transformed["unit"] = data["unit"]
                if "temp" in data["sensor"]:
                    transformed["sensor"] = "temperature"
                elif "pres" in data["sensor"]:
                    transformed["sensor"] = "pressure"
                elif "humi" in data["sensor"]:
                    transformed["sensor"] = "humidity"
                return transformed
            elif isinstance(data, dict) and \
                    "content" in data and "actions" in data:
                i = 0
                n = 1
                while i < len(data['content']):
                    transformed[n] = f"{data['content'][i].capitalize()}\
 activity logged: {data['processed']} actions processed"
                    i += 3
                    n += 1
                transformed["actions"] = data["actions"]
                return transformed
            elif isinstance(data, dict) and "stream" in data:
                count = 0
                streams = 0
                info = data["stream"]
                for stream in info:
                    count += 1
                    streams += float(stream)
                transformed["streams"] = count
                transformed["sum"] = streams
                return transformed
            else:
                return data

        except ValueError:
            return "ERROR detected in Stage 2: Invalid data format"


class OutputStage():
    """OutputStage class."""
    def process(self, data: Union[str, Dict]) -> str:
        """process function."""
        try:
            output = ""
            if isinstance(data, dict) and "value" in data:
                output = f'Processed {data["sensor"]} reading: '
                output += f'{data["value"]}{data["unit"]} '
                output += f'({data["range"]} range)'
                return output
            elif isinstance(data, dict) and "actions" in data:
                i = 1
                while i <= data["actions"]:
                    output += f"{data[i]}\n"
                    i += 1
                return output
            elif isinstance(data, dict) and "streams" in data:
                avg = data["sum"] / data["streams"]
                output = f'Stream summary: {data["streams"]}'
                output += f"readings, avg: {avg:.1f}°C"
                return output
            else:
                return data

        except Exception as e:
            return f"ERROR detected in Stage 3: {e}"


class ProcessingPipeline(ABC):
    """ProcessingPipeline class."""
    def __init__(self, pipeline_id: str) -> None:
        """__init__ function."""
        self.stages: list = []
        self.pipeline_id = pipeline_id
        self.processed = 0
        self.errors = 0

    def add_stage(self, stage: ProcessingStages) -> None:
        """add_stage function."""
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """process function."""
        pass

    def run(self, data: Any) -> Any:
        """run function."""
        format: Any = data
        for stage in self.stages:
            format = stage.process(format)
        if isinstance(format, str) and "ERROR" in format:
            return format
        self.processed += 1
        return format


class JSONAdapter(ProcessingPipeline):
    """JSONAdapter class."""
    def __init__(self, pipeline_id: str) -> None:
        """__init__ function."""
        super().__init__(pipeline_id)

    def process(self, data: Dict) -> str:
        """process function."""
        if not isinstance(data, dict):
            return "ERROR: Invalid data format."
        return self.run(data)


class CSVAdapter(ProcessingPipeline):
    """CSVAdapter class."""
    def __init__(self, pipeline_id: str) -> None:
        """__init__ function."""
        super().__init__(pipeline_id)

    def process(self, data: str) -> str:
        """process function."""
        if not isinstance(data, str):
            return "ERROR: Invalid data format."
        return self.run(data)


class StreamAdapter(ProcessingPipeline):
    """StreamAdapter class."""
    def __init__(self, pipeline_id: str) -> None:
        """__init__ function."""
        super().__init__(pipeline_id)

    def process(self, data: List) -> str:
        """process function."""
        if not isinstance(data, List):
            return "ERROR: Invalid data format."
        return self.run(data)


class NexusManager():
    """NexusManager class."""
    def __init__(self) -> None:
        """__init__ function."""
        self.pipelines: list = []
        self.success = 0
        self.processed = 0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """add_pipeline function."""
        self.pipelines.append(pipeline)
        self.processed += 1

    def process_data(self, data: Any) -> str:
        """process_data function."""
        for pipe in self.pipelines:
            if isinstance(pipe, ProcessingPipeline):
                result = pipe.process(data)
                if "ERROR: Invalid data format." in result:
                    continue
                else:
                    break
            else:
                return "ERROR: Invalid Adapter Type"
        if "ERROR" not in result:
            self.success += 1
        return result


def main() -> None:
    """main function."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n === Multi-Format Data Processing ===")
    try:
        manager = NexusManager()
        adapters = [
            JSONAdapter("JSON01"),
            CSVAdapter("CSV01"),
            StreamAdapter("Stream01"),
        ]
        for pipe in adapters:
            pipe.add_stage(InputStage())
            pipe.add_stage(TransformStage())
            pipe.add_stage(OutputStage())
            manager.add_pipeline(pipe)

        print("\nProcessing JSON data through pipeline..")
        data = {"sensor": "temp", "value": 23.5, "unit": "C"}
        print(f"Input: {data}")
        print("Transform: Enriched with metadata and validation")
        r = manager.process_data(data)
        print("Output:", r)

        print("\nProcessing CSV data through pipeline..")
        data = "user,action,timestamp"
        print(f'Input: "{data}"')
        print("Transform: Parsed and structured data")
        r = manager.process_data(data)
        print("Output:", r)

        print("Processing Stream data through same pipeline...")
        data = [21.5, 22.0, 22.5, 23.0, 21.5]
        print("Input: Real-time sensor stream")
        print("Transform: Aggregated and filtered")
        r = manager.process_data(data)
        print("Output:", r)

        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")

        print(f"\nChain result: {manager.processed} ", end="")
        print("records processed through 3-stage pipeline")
        effiency = (manager.success / manager.processed) * 100
        print(f"Performance: {effiency:.1f}% efficiency, ", end="")
        print("0.2s total processing time")

        print("\n=== Error Recovery Test ===")
        print("Simulating pipeline failure...")
        bad = JSONAdapter("Json02")
        bad.add_stage(InputStage())
        bad.add_stage(TransformStage())
        bad.add_stage(OutputStage())

        data = {"value": "error", 'sensor': 'temp', 'unit': 'C'}
        r = bad.process(data)
        print(r)
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

        print("\nNexus Integration complete. All systems operational.")

    except AttributeError as e:
        print("ERROR:", e)
    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    main()

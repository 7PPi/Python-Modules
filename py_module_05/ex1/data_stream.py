from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"Stream ID": self.id,
                "format": f"Stream ID: {self.id}"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Dict]) -> str:
        operations = 0
        avg = 0
        t = 0
        if not isinstance(data_batch, list):
            return "Error: data is not a list."
        for stream in data_batch:
            for key, value in stream.items():
                if key == "temp":
                    avg += float(value)
                    t += 1
                elif key != "humidity" and key != "pressure":
                    return "ERROR: Unknown data type inserted."
                operations += 1
        if t != 0:
            return f"{operations} readings processed, avg temp: {avg / t}°C"
        return f"{operations} readings processed, avg temp: 0°C"

    def filter_data(self, data_batch: List[Dict],
                    criteria: Optional[str] = None) -> List[Dict]:
        if criteria == "high-priority" or criteria == "critical":
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    if isinstance(key, str) and isinstance(value, (int, float))
                    if (key == "temp" and (value >= 15 or value >= 25)
                    or key == "humidity" and (value >= 65 or value >= 32)
                    or key == "pressure" and (value >= 1030 or value >= 1025))
                    ]
        elif criteria == "processor":
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    if isinstance(key, str) and isinstance(value, (int, float))
                    if (key == "temp" or key == "humidity"
                        or key == "pressure")
                    ]
        else:
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    ]

    def get_stats(self) -> Dict:
        stat = super().get_stats()
        stat["final"] = f"{stat['format']}, Type: {self.type}"
        return stat


class TransactionStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Dict]) -> str:
        operations = 0
        net = 0
        for stream in data_batch:
            for key, value in stream.items():
                if key == "buy":
                    net += int(value)
                elif key == "sell":
                    net -= int(value)
                else:
                    return "ERROR: Unknown operations type inserted."
                operations += 1
        if net > 0:
            return f"{operations} operations, net flow: +{net} units"
        else:
            return f"{operations} operations, net flow: {net} units"

    def filter_data(self, data_batch: List[Dict],
                    criteria: Optional[str] = None) -> List[Dict]:
        if criteria == "high-priority" or criteria == "critical":
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    if isinstance(key, str) and isinstance(value, (int, float))
                    if (key == "buy" and value >= 10000
                    or key == "sell" and value >= 10000)
                    ]
        elif criteria == "processor":
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    if isinstance(key, str) and isinstance(value, (int, float))
                    if (key == "buy" or key == "sell")
                    ]
        else:
            return [{key: value}
                    for data in data_batch
                    if isinstance(data, dict)
                    for key, value in data.items()
                    ]

    def get_stats(self) -> Dict:
        stat = super().get_stats()
        stat["final"] = f"{stat['format']}, Type: {self.type}"
        return stat


class EventStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.type = "System Events"

    def process_batch(self, data_batch: List) -> str:
        event = 0
        err = 0
        for stream in data_batch:
            if stream == "error":
                err += 1
            event += 1
        return f"{event} events, {err} error detected"

    def filter_data(self, data_batch: List,
                    criteria: Optional[str] = None) -> List:
        if criteria == "high-priority" or criteria == "critical":
            return [data for data in data_batch
                    if isinstance(data, str)
                    if data in ("login", "logout", "error")
                    ]
        elif criteria == "processor":
            return [data for data in data_batch
                    if isinstance(data, str)
                    if data in ("login", "logout", "error")
                    ]
        else:
            return [data for data in data_batch
                    if isinstance(data, str)
                    ]

    def get_stats(self) -> Dict:
        stat = super().get_stats()
        stat["final"] = f"{stat['format']}, Type: {self.type}"
        return stat


class StreamProcessor():
    def __init__(self, streams: List[Any]) -> None:
        self.streams = streams

    def process_all(self, data_batch: List[Any]) -> None:
        for stream in self.streams:
            filtered = stream.filter_data(data_batch, "processor")
            buf = stream.process_batch(filtered)
            result = ""
            for ch in buf:
                if ch != ",":
                    result += ch
                else:
                    break
            if "readings" in result:
                print("Sensor data:", result)
            elif "operations" in result:
                print(f"Transaction data: {result} processed")
            elif "events" in result:
                print(f"Event data: {result} processed")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(sensor.get_stats()['final'])
    data = [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
    formatted = [f"{key}: {value}" for d in data for key, value in d.items()]
    filtered = sensor.filter_data(data)
    print(f"Processing sensor batch: {formatted}")
    resut = sensor.process_batch(filtered)
    print("Sensor analysis: ", resut)

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(transaction.get_stats()['final'])
    data = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    formatted = [f"{key}:{value}" for d in data for key, value in d.items()]
    filtered = transaction.filter_data(data)
    print(f"Processing transaction batch: {formatted}")
    resut = transaction.process_batch(filtered)
    print("Transaction analysis: ", resut)

    print("\nInitializing Event Stream...")
    event = EventStream("TRANS_001")
    print(f"Stream ID: {event.id}, Type: {event.type}")
    data = ["login", "error", "logout"]
    print(f"Processing event batch: {data}")
    resut = event.process_batch(data)
    print("Event analysis: ", resut)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("\nBatch 1 Results:")

    sensor = SensorStream("SENSOR_002")
    transaction = TransactionStream("TRANS_002")
    event = EventStream("TRANS_002")

    data_batch = ["login",
                  "logout",
                  "login",
                  {"buy": 13000},
                  {"sell": 100},
                  {"sell": 100},
                  {"sell": 100},
                  {"pressure": 1043},
                  {"humidity": 75}]
    processor = StreamProcessor([sensor, transaction, event])
    processor.process_all(data_batch)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: ", end="")
    info = len(sensor.filter_data(data_batch, "critical"))
    print(f"{info} critical sensor alerts, ", end="")
    info = len(transaction.filter_data(data_batch, "critical"))
    print(f"{info} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")

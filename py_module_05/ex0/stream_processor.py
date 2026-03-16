"""Module documentation."""
from abc import ABC, abstractmethod
from typing import List, Any, Optional


class DataProcessor(ABC):
    """DataProcessor class."""
    @abstractmethod
    def process(self, data: Any) -> str:
        """process function."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """validate function."""
        pass

    def format_output(self, result: str) -> str:
        """format_output function."""
        return result


class NumericProcessor(DataProcessor):
    """NumericProcessor class."""
    def process(self, data: List[int]) -> str:
        """process function."""
        try:
            sum = 0
            count = 0
            avg = 0
            for num in data:
                sum += int(num)
                count += 1
            avg = sum / count
            result = f"Processed {count} numeric values, sum={sum}, avg={avg}"
            return self.format_output(result)
        except Exception:
            return ""

    def validate(self, data: List[int]) -> bool:
        """validate function."""
        try:
            for num in data:
                int(num)
        except ValueError:
            print("Validation: ERROR, Non-numeric data detected")
            return False
        except TypeError:
            print("Validation: ERROR, data is not a list")
            return False
        else:
            print("Validation: Numeric data verified")
            return True

    def format_output(self, result: str) -> Optional[str]:
        """format_output function."""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    """TextProcessor class."""
    def process(self, data: str) -> str:
        """process function."""
        try:
            ch = 0
            count = 1
            for c in data:
                if c == ' ':
                    count += 1
                ch += 1
            result = f"Processed text: {ch} characters, {count} words"
            return self.format_output(result)
        except Exception:
            return ""

    def validate(self, data: str) -> bool:
        """validate function."""
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        else:
            print("Validation: ERROR, Non-text data detected")
            return False

    def format_output(self, result: str) -> str:
        """format_output function."""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    """LogProcessor class."""
    def process(self, data: str) -> str:
        """process function."""
        log = ""
        msg = ""
        p = False
        level = ""
        try:
            for c in data:
                if not p:
                    if c == ":":
                        p = True
                    else:
                        log += c
                else:
                    msg += c

            if "ERROR" in log:
                level = "ALERT"
            elif "INFO" in log:
                level = "INFO"
            elif "WARNING" in log:
                level = "WARNING"

            result = f"[{level}] {log} level detected: {msg}"
            return self.format_output(result)
        except Exception:
            return ""

    def validate(self, data: str) -> bool:
        """validate function."""
        log = ""
        msg = ""
        p = False
        if not isinstance(data, str):
            print("Validation: ERROR, Log is not a string")
            return False
        for c in data:
            if not p:
                if c == ":":
                    p = True
                else:
                    log += c
            else:
                msg += c

        if msg is None or not p:
            print("Validation: ERROR, Log does not contain a message")
            return False
        if "ERROR" in log:
            print("Validation: Log entry verified")
            return True
        elif "WARNING" in log:
            print("Validation: Log entry verified")
            return True
        elif "INFO" in log:
            print("Validation: Log entry verified")
            return True
        else:
            print("Validation: ERROR, unknown log format")
            return False

    def format_output(self, result: str) -> str:
        """format_output function."""
        return super().format_output(result)


def main() -> None:
    """main function."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        print("Initializing Numeric Processor...")
        numeric = NumericProcessor()
        data = [1, 2, 3, 4, 5]
        print(f"Processing data: {data}")
        numeric.validate(data)
        result = numeric.process(data)
        print(f"Output: {result}")

        print("\nInitializing Text Processor..")
        text = TextProcessor()
        data = "Hello Nexus World"
        print(f"Processing data: {data}")
        text.validate(data)
        result = text.process(data)
        print(f'Output: "{result}"')

        print("\nInitializing Log Processor...")
        log = LogProcessor()
        data = "ERROR: Connection timeout"
        print(f"Processing data: {data}")
        log.validate(data)
        result = log.process(data)
        print(f"Output: {result}")

        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")
        processors = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor(),
        ]
        samples = [
            [1, 2, 3],
            "Hello world!",
            "INFO level detected: System ready"
        ]
        i = 1
        for processor, data in zip(processors, samples):
            result = processor.process(data)
            print(f"Result {i}: {result}")
            i += 1

        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except TypeError as e:
        print("ERROR: data is not insert,", e)


if __name__ == "__main__":
    main()

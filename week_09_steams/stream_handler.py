from io import BytesIO


class StreamHandler:
    MAX_BUF_SIZE = 1048576  # 1 Mb
    CHUNK_SIZE = 1024  # 1 Kb

    def __init__(self, input_, output):
        """
            input, output - byte streams
        """

        self.input = input_
        self.output = output

        self.buffer = BytesIO()
        self.buf_size = 0

        self.received = 0

    def read(self, size=CHUNK_SIZE):
        return self.input.read(size)

    def handle(self, data):
        return data

    def write(self, data):
        out_size = self.output.write(data)

        if data[out_size:]:
            # Send left data
            out_size += self.write(data[out_size:])
        return out_size

    def flush_buffer(self):
        self.write(self.buffer.getbuffer())
        self.buffer = BytesIO()
        self.buf_size = 0

    def completed(self):
        return False

    def run(self):
        while True:
            # Read data
            data = self.read()
            self.received += len(data)

            # Handle data
            handled_data = self.handle(data)

            # Buffer data
            self.buf_size += self.buffer.write(handled_data)

            # Flush buffer if needed
            if self.buf_size >= self.MAX_BUF_SIZE:
                self.flush_buffer()

            # Check if stream completed
            if self.completed():
                break

        self.flush_buffer()

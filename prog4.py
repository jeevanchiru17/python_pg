import random
import re

from faker import Faker

fake = Faker()

# a) Create synthetic logs (normal + attack)
logs = []

# normal logs
for _ in range(100):
    ip = fake.ipv4()
    status = random.choice([200, 201, 302, 404, 403])
    logs.append(f'{ip} - - [{fake.date_time()}] "GET /home" {status}')

# attack logs: one IP with >15 failures
attacker = fake.ipv4()
for _ in range(20):
    logs.append(f'{attacker} - - [{fake.date_time()}] "POST /login" 401')


# b) LogSentinel class with regex named groups
class LogSentinel:
    pattern = re.compile(
        r"(?P<ip>\d+\.\d+\.\d+\.\d+).*"
        r"\[(?P<time>.*?)\]\s+"
        r'"(?P<method>\w+)\s+(?P<path>.*?)"\s+'
        r"(?P<status>\d+)"
    )

    # c) Parse logs and count client errors 400–499
    def parse(self, log_list):
        counts = {}

        for line in log_list:
            m = self.pattern.search(line)
            if m:
                status = int(m.group("status"))
                if 400 <= status < 500:
                    ip = m.group("ip")
                    counts[ip] = counts.get(ip, 0) + 1

        return counts


# -------- Main Execution --------
sent = LogSentinel()
result = sent.parse(logs)

print("Client Error Counts per IP:")
print(result)

class DataSource:
def read(self):
# Simulação de leitura de dados
return "Dados do relatório"

class ReportGenerator:
def __init__(self, data_source):
self.data_source = data_source

def fetch_data(self):
return self.data_source.read()

def generate_report(self):
data = self.fetch_data()
report = f"Report: {data}"
return report

class ReportHandler:
def handle(self, report):
raise NotImplementedError("Método handle precisa ser implementado")

class FileReportSaver(ReportHandler):
def __init__(self, filename):
self.filename = filename

def handle(self, report):
with open(self.filename, 'w') as f:
f.write(report)

class EmailReportSender(ReportHandler):
def __init__(self, email_address):
self.email_address = email_address

def handle(self, report):
print(f"Sending report to {self.email_address}: {report}")

if __name__ == "__main__":
# Fonte de dados
data_source = DataSource()

report_generator = ReportGenerator(data_source)
report = report_generator.generate_report()

file_saver = FileReportSaver("report.txt")
file_saver.handle(report)

email_sender = EmailReportSender("example@example.com")
email_sender.handle(report)
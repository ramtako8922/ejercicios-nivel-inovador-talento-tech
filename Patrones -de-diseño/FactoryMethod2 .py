from abc import ABC, abstractmethod

# Clase base para definir un reporte
class Reporte(ABC):
    @abstractmethod
    def generar(self):
        pass

# Clases concretas que representan diferentes tipos de reportes
class ReportePDF(Reporte):
    def generar(self):
        return "Generando reporte en formato PDF"

class ReporteCSV(Reporte):
    def generar(self):
        return "Generando reporte en formato CSV"

# Clase fábrica abstracta para crear reportes
class FabricaReportes(ABC):
    @abstractmethod
    def crear_reporte(self):
        pass

# Clases concretas de fábrica que crean reportes específicos
class FabricaReportesPDF(FabricaReportes):
    def crear_reporte(self):
        return ReportePDF()

class FabricaReportesCSV(FabricaReportes):
    def crear_reporte(self):
        return ReporteCSV()

# Uso
fabrica_pdf = FabricaReportesPDF()
reporte_pdf = fabrica_pdf.crear_reporte()
print(reporte_pdf.generar())  # Output: Generando reporte en formato PDF

fabrica_csv = FabricaReportesCSV()
reporte_csv = fabrica_csv.crear_reporte()
print(reporte_csv.generar())  # Output: Generando reporte en formato CSV

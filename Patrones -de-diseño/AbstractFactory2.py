# Interfaz para la fábrica abstracta de reportes
class FabricaReportes:
    def crear_reporte(self):
        pass

# Interfaz para reportes
class Reporte:
    def generar(self):
        pass

# Clases concretas que implementan la fábrica abstracta y los reportes
class FabricaReportesPDF(FabricaReportes):
    def crear_reporte(self):
        return ReportePDF()

class FabricaReportesCSV(FabricaReportes):
    def crear_reporte(self):
        return ReporteCSV()

class ReportePDF(Reporte):
    def generar(self):
        return "Generando reporte en formato PDF"

class ReporteCSV(Reporte):
    def generar(self):
        return "Generando reporte en formato CSV"

# Uso
fabrica_pdf = FabricaReportesPDF()
reporte_pdf = fabrica_pdf.crear_reporte()
print(reporte_pdf.generar())  # Output: Generando reporte en formato PDF

fabrica_csv = FabricaReportesCSV()
reporte_csv = fabrica_csv.crear_reporte()
print(reporte_csv.generar())  # Output: Generando reporte en formato CSV

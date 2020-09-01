import json
import webbrowser

with open("data.json") as file:
    data = json.load(file)
    f = open('Reporte.html','w')
    mensaje = """<!DOCTYPE html>
        <html>
        <head>
            <title>Reporte</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        </head>
        <body background="img/textura.jpg">
        <h1 style="text-align:center">REPORTE DE REGISTROS</h1>
        <div class="row">
        <div class="col"></div>
        <div class="col-8">        
        <table class="table table-hover table-success">
            <thead class="thead-dark">
                <tr>
                    <th>Nombre</th>
                    <th>Edad</th>
                    <th>Activo</th>
                    <th>Saldo</th>
                </tr>
            </thead>"""                
    for client in data['personas']:
        mensaje = mensaje + """
        <tr>
            <td>"""+client['nombre']+"""</td>
            <td>"""+client['edad']+"""</td>
            <td>"""+client['activo']+"""</td>
            <td>"""+client['saldo']+"""</td>
        </tr>
        """
mensaje = mensaje + """</table></div>
<div class="col"></div>
</div>
</body>
</html>"""
f.write(mensaje)
f.close()
webbrowser.open_new_tab('Reporte.html')
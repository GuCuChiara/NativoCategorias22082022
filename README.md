<h1>Buscador</h1>
<h2>Prototipo de buscador de diagnósticos y prestaciones asociadas</>
<h3>Descripción general</h3>
        <div class="card-body">
          <p class="card-text">
            <p>Este modelo de prueba funciona con una base de datos implementada con PostgreSQL</p>
            <ul>
             <p>-Tabla con códigos CIE10 ampliado (12542 filas)</p>
             <p>-Tabla con códigos Sancor (prestaciones cargadas en este modelo: 205)</p>
             <p>-Tabla intermedia que vincula las claves primarias de las 2 anteriores (relación muchos a muchos (15315 filas))</p>
             <p>-Backend y frontend desarrollado con Django (Python, HTML5, Javascript, Boostrap 5, jquery 3.6)</p>
             <p>-Base de datos desarrollada en PostgreSQL ver. 14.4</p>
             <p></p>
            <p></p>
            <hr>
            <h3>Se jerarquizaron los códigos de CIE10 en la búsqueda:</h3>
            <h4>Categorías (determinan el orden de aparición):</h4>
             </ul>
            </p>
             <table class="table">
              <tr>
                <th>Categoría</th>
                <th>Cantidad de caracteres, contando el (.)</th>
                <th>Ejemplo código</th>
                <th>Ejemplo descripción</th>
              </tr>
              <tr>
                <td>1</td>
                <td>3 caracteres</td>
                <td>M00</td>
                <td>Artritis piógena (séptica)</td>
              </tr>
              <tr>
                <td>2</td>
                <td>5 caracteres</td>
                <td>M00.0</td>
                <td>Artritis y poliartritis estafilocócica</td>
              </tr>
              <tr>
                <td>2</td>
                <td>5 caracteres</td>
                <td>M13.9</td>
                <td>Artritis, no especificada</td>
              </tr>
              <tr>
                <td>3</td>
                <td>6 caracteres</td>
                <td>M00.01</td>
                <td>Artritis Stafilococo y Polyartitis Región de Hombro</td>
              </tr>
              <tr>
                <td>4</td>
                <td>otros</td>
                <td>M25</td>
                <td>Otros trastornos de articulación, no clasificados bajo otro concepto</td>
              </tr>
              <tr>
                <td>4</td>
                <td>otras</td>
                <td>M12</td>
                <td>Otras artropatías y las no especificadas</td>
              </tr>
            </table>
              
             
            
            

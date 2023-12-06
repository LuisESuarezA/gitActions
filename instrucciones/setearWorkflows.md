## En este documento tenemos los pasos base para setear una acción de gitHub en nuestro repositorio.
1. Primero debemos crear un directorio dentro de nuestro repositorio de la forma especifica: .github/workflows
2. Luego debemos crear un archivo YAML de la forma action.yml en el directorio anterior.
3. Al hacer push a nuestro repositorio en github, se deben actualizar las acciones dentro del repositorio.
4. Podemos probar al accionarlos al usar un evento que lo active. 
* Es importante tomar en cuenta que las acciones deben diseñarse respecto al tipo de archivos que se van a usar.
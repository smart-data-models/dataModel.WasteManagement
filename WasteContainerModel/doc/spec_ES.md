Entidad: WasteContainerModel  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)  
Descripción global: **Un modelo de contenedor de residuos que capta las propiedades estáticas de una clase de contenedores.  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `brandName`: El nombre de la marca  - `cargoVolume`: El volumen total que puede contener el contenedor  - `category`: La categoría del contenedor. Enum:'contenedor de basura, cubo de basura, cubo de ruedas, otro'. contenedor de basura. Véase [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color`: El color del producto  - `compliantWith`: Una lista de normas a las que el contenedor cumple (por ejemplo, UNE-EN 840-2:2013).  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `depth`: La profundidad del contenedor  - `description`: Una descripción de este artículo  - `features`: Una lista de características del contenedor. Enum:'ruedas, tapa, tapa redondeada, agujeros de inserción, cerrable'. Cualquier otro valor significativo para la aplicación.  - `height`: La altura del contenedor  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `insertHolesNumber`: Número de agujeros de inserción que tiene el contenedor  - `madeOf`: Material del que está hecho el contenedor. Enum:' plástico, madera, metal, otros'.  - `madeOfCode`: Código de material según las tablas estándar.  - `manufacturerName`: Nombre del fabricante.  - `maximumLoad`: La carga máxima que el contenedor puede soportar con seguridad. Unidad:'Kilogramo'.  - `modelName`: Nombre del modelo según lo indicado por el fabricante. Este atributo es diferente del nombre que es sólo un nombre en clave dado normalmente por los municipios.  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `recommendedLoad`: La carga recomendada por el fabricante para el contenedor. Unidad:'Kilogramo'.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI: Tiene que ser WasteContainerModel  - `weight`: El peso del contenedor  - `width`: Ancho del contenedor    
Propiedades requeridas  
- `id`  - `name`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerModel:    
  description: 'A model of waste container which captures the static properties of a class of containers.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    brandName:    
      description: 'Name of the brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand    
    cargoVolume:    
      description: 'Total volume the container can hold'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
    category:    
      description: 'Container’s category. Enum:''dumpster, trashCan, wheelieBin, other''.  dumpster . See [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)'    
      items:    
        enum:    
          - dumpster    
          - trashCan    
          - wheelieBin    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    compliantWith:    
      description: 'A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013). '    
      items:    
        type: string    
      minItems: 0    
      type: Property    
      uniqueItems: true    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      description: 'Depth of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
        units: Meters    
    description:    
      description: 'A description of this item'    
      type: Property    
    features:    
      description: 'A list of container features. Enum:''wheels, lid, roundedLid, insertHoles, lockable''. Any other value meaningful for the application.'    
      items:    
        enum:    
          - wheels    
          - lid    
          - roundedLid    
          - insertHoles    
          - lockable    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    height:    
      description: 'Height of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/heigth    
        units: Meters    
    id:    
      anyOf: &wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    insertHolesNumber:    
      description: 'Number of insert holes the container has'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    madeOf:    
      description: 'Material the container is made of. Enum:'' plastic , wood, metal, other '''    
      enum:    
        - plastic    
        - wood    
        - metal    
        - other    
      type: Property    
    madeOfCode:    
      description: 'Material Code as per standard tables. '    
      type: Property    
    manufacturerName:    
      description: 'Name of the manufacturer. '    
      type: Property    
    maximumLoad:    
      description: 'Maximum load the container can hold safely. Unit:''Kilogram'''    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    modelName:    
      description: 'Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities.'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    recommendedLoad:    
      description: 'Manufacturer recommended load for the container. Unit:''Kilogram'''    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be WasteContainerModel'    
      enum:    
        - WasteContainerModel    
      type: Property    
    weight:    
      description: 'Weight of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weigth    
        units: Kilograms    
    width:    
      description: 'Width of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: Meters    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### WasteContainerModel NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un WasteContainerModel en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "width": 0.5,  
  "height": 0.8,  
  "depth": 0.4,  
  "cargoVolume": 150,  
  "brandName": "Brute",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "modelName": "C1",  
  "compliantWith": ["UNE-EN 840-2:2013"],  
  "madeOf": "plastic",  
  "features": ["wheels", "lid"],  
  "category": ["dumpster"]  
}  
```  
#### WasteContainerModel NGSI V2 normalizado Ejemplo  
He aquí un ejemplo de un WasteContainerModel en formato JSON normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "value": ["dumpster"]  
  },  
  "cargoVolume": {  
    "value": 150  
  },  
  "modelName": {  
    "value": "C1"  
  },  
  "name": {  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "compliantWith": {  
    "value": ["UNE-EN 840-2:2013"]  
  },  
  "madeOf": {  
    "value": "plastic"  
  },  
  "height": {  
    "value": 0.8  
  },  
  "width": {  
    "value": 0.5  
  },  
  "depth": {  
    "value": 0.4  
  },  
  "brandName": {  
    "value": "Brute"  
  },  
  "features": {  
    "value": ["wheels", "lid"]  
  }  
}  
```  
#### WasteContainerModelo NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de un WasteContainerModel en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Brute",  
 "cargoVolume": 150,  
 "category": ["dumpster"],  
 "compliantWith": ["UNE-EN 840-2:2013"],  
 "depth": 0.4,  
 "features": ["wheels", "lid"],  
 "height": 0.8,  
 "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
 "madeOf": "plastic",  
 "modelName": "C1",  
 "name": "Dumpster_Brute_2009_Plastic_Green",  
 "type": "WasteContainerModel",  
 "width": 0.5}  
```  
#### WasteContainerModel NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un WasteContainerModel en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
    "type": "WasteContainerModel",  
    "category": {  
        "type": "Property",  
        "value": [  
            "dumpster"  
        ]  
    },  
    "cargoVolume": {  
        "type": "Property",  
        "value": 150  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "C1"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Dumpster_Brute_2009_Plastic_Green"  
    },  
    "compliantWith": {  
        "type": "Property",  
        "value": [  
            "UNE-EN 840-2:2013"  
        ]  
    },  
    "madeOf": {  
        "type": "Property",  
        "value": "plastic"  
    },  
    "height": {  
        "type": "Property",  
        "value": 0.8  
    },  
    "width": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "depth": {  
        "type": "Property",  
        "value": 0.4  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Brute"  
    },  
    "features": {  
        "type": "Property",  
        "value": [  
            "wheels",  
            "lid"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  

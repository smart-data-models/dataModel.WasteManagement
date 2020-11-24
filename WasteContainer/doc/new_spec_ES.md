Entidad: WasteContainer  
=======================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Un contenedor de residuos**  

## Lista de propiedades  

`TimeInstant`:   `actuationHours`:   `address`: La dirección postal.  `alternateName`: Un nombre alternativo para este artículo  `annotations`:   `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `cargoWeight`:   `category`:   `color`: El color del producto.  `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateLastCleaning`:   `dateLastEmptying`:   `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateServiceStarted`:   `description`: Una descripción de este artículo  `fillingLevel`:   `id`:   `image`: Una imagen del artículo.  `isleId`:   `location`:   `methaneConcentration`:   `name`: El nombre de este artículo.  `nextActuationDeadline`:   `nextCleaningDeadline`:   `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `refDevice`:   `refWasteContainerIsle`:   `refWasteContainerModel`:   `regulation`:   `responsible`:   `seeAlso`:   `serialNumber`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `status`:   `storedWasteCode`:   `storedWasteKind`:   `storedWasteOrigin`:   `temperature`:   `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
WasteContainer:    
  description: 'A waste container'    
  properties:    
    TimeInstant:    
      format: date-time    
      type: string    
    actuationHours:    
      type: string    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    cargoWeight:    
      minimum: 0    
      type: number    
    category:    
      items:    
        enum:    
          - fixed    
          - underground    
          - ground    
          - portable    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    color:    
      description: 'The color of the product.'    
      type: string    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastCleaning:    
      format: date-time    
      type: string    
    dateLastEmptying:    
      format: date-time    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      format: date-time    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    fillingLevel:    
      maximum: 1    
      minimum: 0    
      type: number    
    id:    
      anyOf: &wastecontainer_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    isleId:    
      type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    methaneConcentration:    
      minimum: 0    
      type: number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nextActuationDeadline:    
      format: date-time    
      type: string    
    nextCleaningDeadline:    
      format: date-time    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refDevice:    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
      minItems: 1    
      type: array    
      uniqueItems: true    
    refWasteContainerIsle:    
      anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
    refWasteContainerModel:    
      anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
    regulation:    
      type: string    
    responsible:    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    serialNumber:    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      enum:    
        - ok    
        - lidOpen    
        - dropped    
        - moved    
        - bandalized    
        - burning    
        - unknown    
      type: string    
    storedWasteCode:    
      type: string    
    storedWasteKind:    
      enum:    
        - organic    
        - inorganic    
        - glass    
        - oil    
        - plastic    
        - metal    
        - paper    
        - batteries    
        - electronics    
        - hazardous    
        - other    
      type: string    
    storedWasteOrigin:    
      enum:    
        - household    
        - municipal    
        - industrial    
        - construction    
        - hostelry    
        - agriculture    
        - other    
      type: string    
    temperature:    
      type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WasteContainer    
      type: string    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainer:Fleming:12a",  
  "type": "WasteContainer",  
  "refWasteContainerModel": "wastecontainermodel:c1",  
  "refWasteContainerIsle": "wastecontainerisle:Fleming:12",  
  "serialNumber": "ab56kjl",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.164485591715449, 40.62785133667262]  
  },  
  "temperature": 23,  
  "fillingLevel": 0.4,  
  "dateLastEmptying": "2016-06-21T15:05:59.408Z",  
  "nextActuationDeadline": "2016-06-28T15:05:59.408Z",  
  "status": "ok",  
  "category": ["underground"],  
  "refDevice": ["device-Fleming:12a:1"]  
}  
```  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON normalizado. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainer:Fleming:12a",  
  "type": "WasteContainer",  
  "status": {  
    "value": "ok"  
  },  
  "category": {  
    "value": ["underground"]  
  },  
  "dateLastEmptying": {  
    "type": "DateTime",  
    "value": "2016-06-21T15:05:59.408Z"  
  },  
  "serialNumber": {  
    "value": "ab56kjl"  
  },  
  "nextActuationDeadline": {  
    "value": "2016-06-28T15:05:59.408Z"  
  },  
  "refWasteContainerIsle": {  
    "type": "Relationship",  
    "value": "wastecontainerisle:Fleming:12"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": ["device-Fleming:12a:1"]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.164485591715449, 40.62785133667262]  
    }  
  },  
  "temperature": {  
    "value": 23  
  },  
  "fillingLevel": {  
    "value": 0.4  
  },  
  "refWasteContainerModel": {  
    "type": "Relationship",  
    "value": "wastecontainermodel:c1"  
  }  
}  
```  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "category": ["underground"],  
 "dateLastEmptying": {"@type": "DateTime",  
                      "@value": "2016-06-21T15:05:59.408Z"},  
 "fillingLevel": 0.4,  
 "id": "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "nextActuationDeadline": "2016-06-28T15:05:59.408Z",  
 "refDevice": ["urn:ngsi-ld:Device:device-Fleming:12a:1"],  
 "refWasteContainerIsle": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
 "refWasteContainerModel": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
 "serialNumber": "ab56kjl",  
 "status": "ok",  
 "temperature": 23,  
 "type": "WasteContainer"}  
```  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
    "type": "WasteContainer",  
    "status": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "underground"  
        ]  
    },  
    "dateLastEmptying": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-06-21T15:05:59.408Z"  
        }  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "ab56kjl"  
    },  
    "nextActuationDeadline": {  
        "type": "Property",  
        "value": "2016-06-28T15:05:59.408Z"  
    },  
    "refWasteContainerIsle": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12"  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Device:device-Fleming:12a:1"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.164485591715449,  
                40.62785133667262  
            ]  
        }  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 23  
    },  
    "fillingLevel": {  
        "type": "Property",  
        "value": 0.4  
    },  
    "refWasteContainerModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  

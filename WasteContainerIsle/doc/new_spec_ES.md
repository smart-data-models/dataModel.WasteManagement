Entidad: WasteContainerIsle  
===========================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Una isla de contenedores de residuos**  

## Lista de propiedades  

`address`: La dirección postal.  `alternateName`: Un nombre alternativo para este artículo  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `features`:   `id`:   `insertHolesNumber`:   `location`:   `name`: El nombre de este artículo.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `refWasteContainer`:   `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
WasteContainerIsle:    
  description: 'A waste container isle'    
  properties:    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    features:    
      items:    
        enum:    
          - containerFix    
          - underground    
          - fenced    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    id:    
      anyOf: &wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    insertHolesNumber:    
      minimum: 0    
      type: number    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refWasteContainer:    
      items:    
        anyOf: *wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
      minItems: 1    
      type: array    
      uniqueItems: true    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - WasteContainerIsle    
      type: string    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
Aquí hay un ejemplo de una Isla de Contenedores de Residuos en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainerisle:Fleming:12",  
  "type": "WasteContainerIsle",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [-3.164485591715449, 40.62785133667262],  
        [-3.164445130316209, 40.627871567372239],  
        [-3.164394553567159, 40.627772099765778],  
        [-3.164424899616589, 40.62775018317452],  
        [-3.164485591715449, 40.62785133667262]  
      ]  
    ]  
  },  
  "address": {  
    "streetAddress": "Calle Dr. Fleming, 12",  
    "addressLocality": "Guadalajara",  
    "addressCountry": "ES"  
  },  
  "features": ["underground"],  
  "name": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo",  
  "description": "Container isle located downtown",  
  "refWasteContainer": [  
    "wastecontainer:Fleming:12a",  
    "wastecontainer:Fleming:12b"  
  ]  
}  
```  
He aquí un ejemplo de una Isla de Contenedores de Residuos en formato JSON normalizado. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "wastecontainerisle:Fleming:12",  
  "type": "WasteContainerIsle",  
  "refWasteContainer": {  
    "type": "Relationship",  
    "value": ["wastecontainer:Fleming:12a", "wastecontainer:Fleming:12b"]  
  },  
  "features": {  
    "value": ["underground"]  
  },  
  "description": {  
    "value": "Container isle located downtown"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [-3.164485591715449, 40.62785133667262],  
          [-3.164445130316209, 40.62787156737224],  
          [-3.164394553567159, 40.62777209976578],  
          [-3.164424899616589, 40.62775018317452],  
          [-3.164485591715449, 40.62785133667262]  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Guadalajara",  
      "addressCountry": "ES",  
      "streetAddress": "Calle Dr. Fleming, 12"  
    }  
  },  
  "name": {  
    "value": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo"  
  }  
}  
```  
Aquí hay un ejemplo de una Isla de Contenedores de Residuos en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Guadalajara",  
             "streetAddress": "Calle Dr. Fleming, 12",  
             "type": "PostalAddress"},  
 "description": "Container isle located downtown",  
 "features": ["underground"],  
 "id": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
 "location": {"coordinates": [[[-3.164485591715449, 40.62785133667262],  
                               [-3.164445130316209, 40.62787156737224],  
                               [-3.164394553567159, 40.62777209976578],  
                               [-3.164424899616589, 40.62775018317452],  
                               [-3.164485591715449, 40.62785133667262]]],  
              "type": "Polygon"},  
 "name": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo",  
 "refWasteContainer": ["urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
                       "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12b"],  
 "type": "WasteContainerIsle"}  
```  
He aquí un ejemplo de una Isla de Contenedores de Residuos en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
    "type": "WasteContainerIsle",  
    "refWasteContainer": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
            "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12b"  
        ]  
    },  
    "features": {  
        "type": "Property",  
        "value": [  
            "underground"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Container isle located downtown"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    [  
                        -3.164485591715449,  
                        40.62785133667262  
                    ],  
                    [  
                        -3.164445130316209,  
                        40.62787156737224  
                    ],  
                    [  
                        -3.164394553567159,  
                        40.62777209976578  
                    ],  
                    [  
                        -3.164424899616589,  
                        40.62775018317452  
                    ],  
                    [  
                        -3.164485591715449,  
                        40.62785133667262  
                    ]  
                ]  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Guadalajara",  
            "addressCountry": "ES",  
            "streetAddress": "Calle Dr. Fleming, 12",  
            "type": "PostalAddress"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  

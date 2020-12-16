Entidad: WasteContainer  
=======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
Descripción global: **Un contenedor de residuos**  

## Lista de propiedades  

- `TimeInstant`: Puede haber ambientes de producción donde el tipo de atributo es igual a la cadena "ISO 8601". Si es así, debe ser considerado como un sinónimo de "DateTime".  - `actuationHours`: Horas adecuadas para realizar actuaciones sobre el contenedor.  - `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `cargoWeight`: El peso de la carga del contenedor.  - `category`:   - `color`: El color del producto  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateLastCleaning`: Cuando el contenedor fue limpiado la última vez.  - `dateLastEmptying`: Sello de tiempo que representa cuando el contenedor fue vaciado la última vez.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `dateServiceStarted`: Fecha en la que el contenedor comenzó a dar servicio.  - `description`: Una descripción de este artículo  - `fillingLevel`: Nivel de llenado del contenedor  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `isleId`: Identificador (o nombre) de la isla donde se coloca el contenedor. Este atributo debe utilizarse cuando las entidades de tipo "WasteContainerIsle" no se modelan específicamente. De lo contrario, debe utilizarse "refWasteContainerIsle".  - `location`:   - `methaneConcentration`: Concentración de metano (CH4) dentro del contenedor.  - `name`: El nombre de este artículo.  - `nextActuationDeadline`: Fecha límite para la siguiente actuación a realizar (vaciado, recogida, etc.).  - `nextCleaningDeadline`: Fecha límite para la próxima limpieza.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refDevice`: Referencia al dispositivo o dispositivos utilizados para vigilar este contenedor  - `refWasteContainerIsle`: Isla donde se coloca el contenedor  - `refWasteContainerModel`: El modelo del contenedor  - `regulation`: Reglamento de funcionamiento del contenedor  - `responsible`: Responsable del contenedor, es decir, entidad encargada de actuar (vaciar, recoger, etc.)  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `serialNumber`: Número de serie del contenedor.  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `status`: El estado del contenedor desde el punto de vista de la seguridad. Enum:'ok , tapaAbrir , soltar , mover , vandalizar , quemar , desconocido'.  - `ok`. El contenedor está donde debe estar y se mantiene correctamente. "Tapa abierta". La tapa del contenedor se ha abierto y no se ha cerrado después de un cierto tiempo. "Se ha caído". El contenedor se ha caído por alguna razón. "movido". El contenedor ha sido movido de su posición normal y no ha vuelto. "vandalizado". El contenedor ha sido dañado o destruido debido al vandalismo. "Quemado". El contenedor se está quemando y hay que tomar una acción inmediata. "Desconocido". El estado del contenedor no es conocido por el sistema.  - `storedWasteCode`: Depende de la regulación del objetivo. Para Europa, consulte [la Lista Europea de Residuos] (http://ec.europa.eu/environment/waste/framework/list.htm).  - `storedWasteKind`: Tipo/s de residuos almacenados por el contenedor. Enum:'orgánico, inorgánico, vidrio, aceite, plástico, metal, papel, pilas, electrónica, peligroso, otros'. O cualquier otro valor que no encaje dentro del primero.  - `storedWasteOrigin`: Origen de los residuos almacenados. Enum:'doméstico, municipal, industrial, construcción, hostelería, agricultura, otros'.  - `temperature`: La temperatura dentro del contenedor  - `type`: Tipo de entidad NGSI: Tiene que ser WasteContainer    
Propiedades requeridas  
- `id`  - `location`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainer:    
  description: 'A waste container'    
  properties:    
    TimeInstant:    
      description: 'There can be production environmments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    actuationHours:    
      description: 'Hours suitable for performing actuations over the container.'    
      type: Property    
      x-ngsi:    
        model: openingHours    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    cargoWeight:    
      description: 'Weight of the container load.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    category:    
      description: ""    
      items:    
        enum:    
          - fixed    
          - underground    
          - ground    
          - portable    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: 'https://schema.org/Text Containers category.'    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastCleaning:    
      description: 'When the container was cleaned last time. '    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastEmptying:    
      description: 'Timestamp which represents when the container was emptied last time.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      description: 'Date at which the container started giving service.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
    description:    
      description: 'A description of this item'    
      type: Property    
    fillingLevel:    
      description: 'Filling level of the container'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    isleId:    
      description: 'Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used.'    
      type: Property    
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
      description: 'Methane (CH4) concentration inside the container.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nextActuationDeadline:    
      description: 'Deadline for next actuation to be performed (emptying, picking up, etc.).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    nextCleaningDeadline:    
      description: 'Deadline for next cleaning.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this container'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/URL    
    refWasteContainerIsle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Isle where the container is placed'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    refWasteContainerModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Container''s model'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    regulation:    
      description: 'Regulation under which the container is operating'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    responsible:    
      description: 'Responsible for the container, i.e. entity in charge of  actuating (emptying, collecting, etc)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    serialNumber:    
      description: 'Serial number of the container.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/serialNumber    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      description: 'Container''s status from the point of view of safety. Enum:''ok , lidOpen , dropped , moved , vandalized , burning , unknown''.  -   `ok`. Container is where it must be and stands properly. `lidOpen`. Container''s lid has been opened and not closed after a certain amount of time. `dropped`. Container has been dropped for some reason. `moved`. Container has been moved from its regular position and has not come back. `vandalized`. Container has been damaged or destroyed due to vandalism. `burning`. Container is burning and an immediate action has to be taken. `unknown`. The status of the container is not known to the system.'    
      enum:    
        - ok    
        - lidOpen    
        - dropped    
        - moved    
        - vandalized    
        - burning    
        - unknown    
      type: Property    
    storedWasteCode:    
      description: 'Depend on the target regulation. For Europe, check [Europe''s List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm).'    
      type: Property    
      x-ngsi:    
        model: 'https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind'    
    storedWasteKind:    
      description: 'Kind/s of waste stored by the container. Enum:''organic, inorganic, glass, oil, plastic, metal, paper, batteries, electronics, hazardous, other''. Or any other value which does not fit within the former. '    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    storedWasteOrigin:    
      description: 'Origin of the waste stored. Enum:''household, municipal, industrial, construction, hostelry, agriculture, other'' '    
      enum:    
        - household    
        - municipal    
        - industrial    
        - construction    
        - hostelry    
        - agriculture    
        - other    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    temperature:    
      description: 'Temperature inside the container'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    type:    
      description: 'NGSI Entity Type: It has to be WasteContainer'    
      enum:    
        - WasteContainer    
      type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Contenedor de residuos NGSI V2 valores clave Ejemplo  
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
#### Contenedor de desechos NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Contenedor de residuos NGSI-LD Valores clave Ejemplo  
Aquí hay un ejemplo de un Contenedor de Residuos en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Contenedor de residuos NGSI-LD normalizado Ejemplo  
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

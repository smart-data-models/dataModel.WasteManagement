<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: WasteContainer  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un contenedor de residuos**  
versión: 0.3.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `RFID[string]`: Proporciona el ID del lector RFID.  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: Horas adecuadas para realizar actuaciones sobre el contenedor.  . Model: [openingHours](openingHours)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `annotations[array]`: Anotaciones sobre el artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: Capacidad total en términos de volumen de residuos que puede contener el contenedor.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: Color del contenedor. Puede utilizarse para indicar el tipo de residuos. El código de colores debe seguir las convenciones aplicables a la zona geográfica en la que se encuentran los contenedores.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: El nivel de umbral de llenado del contenedor definido como el nivel (en términos de porcentaje) en el que se generará la alerta o notificación de contenedor lleno.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: Identificación del contenedor de residuos  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[string]`: Hora en que se registró por última vez el nivel del contenedor.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: Carga máxima (peso) que puede soportar la papelera.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: Carga recomendada (peso) que puede soportar la papelera correspondiente a esta observación.  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: Peso de la carga del contenedor.  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Enum:' fijo, suelo, otro, portátil, subterráneo'  . Model: [https://schema.org/Text Containers category](https://schema.org/Text Containers category)- `color[string]`: El color del producto  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateLastCleaning[string]`: Cuando se limpió el contenedor por última vez.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[string]`: Marca de tiempo que representa cuándo se vació el contenedor por última vez.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateServiceStarted[string]`: Fecha en la que el contenedor comenzó a dar servicio.  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: Una descripción de este artículo  - `fillingLevel[number]`: Nivel de llenado del contenedor  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `image[string]`: Una imagen del artículo  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: Identificador (o nombre) de la isla donde se encuentra el contenedor. Este atributo debe utilizarse cuando las entidades de tipo `WasteContainerIsle` no están siendo modeladas específicamente. En caso contrario, debe utilizarse `refWasteContainerIsle`.  - `license_plate[string]`: Indica el número de matrícula del vehículo. Igual que: campo 'license_plate' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `methaneConcentration[number]`: Concentración de metano (CH4) en el interior del contenedor.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `nextActuationDeadline[string]`: Fecha límite para realizar la siguiente actuación (vaciado, recogida, etc.).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[string]`: Fecha límite para la próxima limpieza.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice[array]`: Referencia al dispositivo o dispositivos utilizados para supervisar este contenedor  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: Isla en la que se encuentra el contenedor  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: Modelo de contenedor  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: Reglamento bajo el cual opera el contenedor  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: Responsable del contenedor, es decir, entidad encargada de actuar (vaciar, recoger, etc.)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `serialNumber[string]`: Número de serie del contenedor.  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status[string]`: Estado del contenedor desde el punto de vista de la seguridad. Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. El contenedor está donde debe estar y se encuentra correctamente. `lidOpen`. La tapa del contenedor se ha abierto y no se ha cerrado después de un tiempo determinado. `dropped`. El contenedor se ha caído por alguna razón. `moved`. El contenedor se ha movido de su posición habitual y no ha vuelto. `vandalizado`. El contenedor ha sido dañado o destruido debido al vandalismo. `quemado`. El contenedor está ardiendo y hay que tomar una medida inmediata. `desconocido`. El sistema desconoce el estado del contenedor.  - `storedWasteCode[string]`: Depende de la normativa de destino. Para Europa, consulte [Lista europea de residuos](http://ec.europa.eu/environment/waste/framework/list.htm).  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: Tipo/s de residuos almacenados por el contenedor. Enum:'orgánicos, inorgánicos, vidrio, aceite, plástico, metal, papel, pilas, electrónicos, peligrosos, otros'. O cualquier otro valor que no encaje en el anterior.  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: Origen de los residuos almacenados. Enum:'doméstico, municipal, industrial, construcción, hostelería, agricultura, otros'  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: Temperatura en el interior del contenedor  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[string]`: Marca de tiempo de la carga útil . Puede haber entornos de producción en los que el tipo de atributo sea igual a la cadena `ISO8601`. Si es así, debe considerarse como un sinónimo de `DateTime`. Este atributo se mantiene por compatibilidad con las antiguas implementaciones de referencia de FIWARE.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: Tipo de entidad NGSI: Tiene que ser WasteContainer  - `wardId[string]`: Id de sala de la entidad correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainer:    
  description: 'A waste container'    
  properties:    
    RFID:    
      description: 'Gives the ID of the RFID reader.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    actuationHours:    
      description: 'Hours suitable for performing actuations over the container.'    
      type: string    
      x-ngsi:    
        model: openingHours    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binCapacity:    
      description: 'Total capacity in terms of the volume of waste the bin can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binColor:    
      description: 'Color of the bin. Could be used for indicating the type of waste. The color coding should follow the conventions applicable to the geographical area the bins are located.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binFullnessThreshold:    
      description: 'The fullness threshold level of the bin defined as the level (in terms of percentage) when the bin full alert or notification will be generated.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binId:    
      description: 'Id of the waste carrying bin'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binLoggedTime:    
      description: 'Time when the bin''s level was last logged.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binMaxLoad:    
      description: 'Maximum load (weight) that the waste bin can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binRecommendedLoad:    
      description: 'Recommended load (weight) that the waste bin corresponding to this observation can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: 'Weight of the container load.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    category:    
      description: 'Enum:'' fixed, ground, other, portable, underground'''    
      items:    
        enum:    
          - fixed    
          - ground    
          - other    
          - portable    
          - underground    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: 'https://schema.org/Text Containers category'    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastCleaning:    
      description: 'When the container was cleaned last time. '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastEmptying:    
      description: 'Timestamp which represents when the container was emptied last time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateServiceStarted:    
      description: 'Date at which the container started giving service.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fillingLevel:    
      description: 'Filling level of the container'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    isleId:    
      description: 'Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used.'    
      type: string    
      x-ngsi:    
        type: Property    
    license_plate:    
      description: "Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: GeoProperty    
    methaneConcentration:    
      description: 'Methane (CH4) concentration inside the container.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nextActuationDeadline:    
      description: 'Deadline for next actuation to be performed (emptying, picking up, etc.).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    nextCleaningDeadline:    
      description: 'Deadline for next cleaning.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this container'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
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
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
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
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    regulation:    
      description: 'Regulation under which the container is operating'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    responsible:    
      description: 'Responsible for the container, i.e. entity in charge of  actuating (emptying, collecting, etc)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serialNumber:    
      description: 'Serial number of the container.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
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
      type: string    
      x-ngsi:    
        type: Property    
    storedWasteCode:    
      description: 'Depend on the target regulation. For Europe, check [Europe''s List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm).'    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind'    
        type: Property    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    temperature:    
      description: 'Temperature inside the container'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be WasteContainer'    
      enum:    
        - WasteContainer    
      type: string    
      x-ngsi:    
        type: Property    
    wardId:    
      description: 'Ward Id of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainer/schema.json    
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### Ejemplo de valores clave de WasteContainer NGSI-v2  
Aquí hay un ejemplo de un WasteContainer en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "location": {  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ],  
    "type": "Point"  
  },  
  "binCapacity": 43,  
  "binColor": "Green",  
  "binClearedTime": "2021-03-11T15:51:02+05:30",  
  "wardId": "21",  
  "binCategory": "Household Bin",  
  "license_plate": "KA23F2345",  
  "RFID": "67855734",  
  "binFillingLevel": 0.65,  
  "binFullnessThreshold": 80,  
  "binRecommendedLoad": 30,  
  "binId": "12",  
  "binMaxLoad": 75,  
  "binLoggedTime": "2021-03-01T15:51:02+05:30"  
}  
```  
</details>  
#### WasteContainer NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un WasteContainer en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ],  
      "type": "Point"  
    }  
  },  
  "binCapacity": {  
    "type": "number",  
    "value": 43  
  },  
  "binColor": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "binClearedTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "21"  
  },  
  "binCategory": {  
    "type": "Text",  
    "value": "Household Bin"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA23F2345"  
  },  
  "RFID": {  
    "type": "Text",  
    "value": "67855734"  
  },  
  "binFillingLevel": {  
    "type": "number",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "number",  
    "value": 80  
  },  
  "binRecommendedLoad": {  
    "type": "number",  
    "value": 30  
  },  
  "binId": {  
    "type": "Text",  
    "value": "12"  
  },  
  "binMaxLoad": {  
    "type": "number",  
    "value": 75  
  },  
  "binLoggedTime": {  
    "type": "DateTime",  
    "value": "2021-03-01T15:51:02+05:30"  
  }  
}  
```  
</details>  
#### WasteContainer NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un WasteContainer en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
    "type": "WasteContainer",  
    "RFID": "67855734",  
    "binCapacity": 43,  
    "binCategory": "Household Bin",  
    "binClearedTime": "2021-03-11T15:51:02+05:30",  
    "binColor": "Green",  
    "binFillingLevel": 0.65,  
    "binFullnessThreshold": 80,  
    "binId": "12",  
    "binLoggedTime": "2021-03-01T15:51:02+05:30",  
    "binMaxLoad": 75,  
    "binRecommendedLoad": 30,  
    "license_plate": "KA23F2345",  
    "location": {  
        "coordinates": [  
            -8.768460000000001,  
            42.60214472222222  
        ],  
        "type": "Point"  
    },  
    "wardId": "21",  
    "@context": [  
        "iudx:WmgmtBin",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WasteContainer NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un WasteContainer en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
    "type": "WasteContainer",  
    "RFID": {  
        "type": "Property",  
        "value": "67855734"  
    },  
    "binCapacity": {  
        "type": "Property",  
        "value": 43  
    },  
    "binCategory": {  
        "type": "Property",  
        "value": "Household Bin"  
    },  
    "binClearedTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "binColor": {  
        "type": "Text",  
        "value": "Green"  
    },  
    "binFillingLevel": {  
        "type": "Property",  
        "value": 0.65  
    },  
    "binFullnessThreshold": {  
        "type": "Property",  
        "value": 80  
    },  
    "binId": {  
        "type": "Property",  
        "value": "12"  
    },  
    "binLoggedTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "binMaxLoad": {  
        "type": "Property",  
        "value": 75  
    },  
    "binRecommendedLoad": {  
        "type": "Property",  
        "value": 30  
    },  
    "license_plate": {  
        "type": "Property",  
        "value": "KA23F2345"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "coordinates": [  
                -8.768460000000001,  
                42.60214472222222  
            ],  
            "type": "Point"  
        }  
    },  
    "wardId": {  
        "type": "Property",  
        "value": "21"  
    },  
    "@context": [  
        "iudx:WmgmtBin",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

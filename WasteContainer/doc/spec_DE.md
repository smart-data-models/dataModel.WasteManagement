Entität: WasteContainer  
=======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Abfallbehälter**  

## Liste der Eigenschaften  

- `TimeInstant`: Es kann Produktionsumgebungen geben, in denen der Attributtyp gleich der Zeichenkette `ISO8601` ist. Wenn dies der Fall ist, muss es als Synonym für `DateTime` betrachtet werden.  - `actuationHours`: Stunden, die für die Durchführung von Betätigungen über dem Behälter geeignet sind.  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `cargoWeight`: Gewicht der Containerladung.  - `category`:   - `color`: Die Farbe des Produkts  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateLastCleaning`: Wann der Behälter das letzte Mal gereinigt wurde.  - `dateLastEmptying`: Zeitstempel, der darstellt, wann der Container das letzte Mal geleert wurde.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateServiceStarted`: Datum, an dem der Container seinen Dienst aufgenommen hat.  - `description`: Eine Beschreibung dieses Artikels  - `fillingLevel`: Füllstand des Behälters  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `isleId`: Bezeichner (oder Name) der Insel, auf der sich der Container befindet. Dieses Attribut sollte verwendet werden, wenn Entitäten vom Typ `WasteContainerIsle` nicht speziell modelliert werden. Andernfalls sollte `refWasteContainerIsle` verwendet werden.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `methaneConcentration`: Methan (CH4)-Konzentration im Inneren des Behälters.  - `name`: Der Name dieses Elements.  - `nextActuationDeadline`: Termin für die nächste auszuführende Betätigung (Entleeren, Aufnehmen, etc.).  - `nextCleaningDeadline`: Deadline für die nächste Reinigung.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `refDevice`: Verweis auf das/die Gerät(e), das/die zur Überwachung dieses Containers verwendet wird/werden  - `refWasteContainerIsle`: Insel, auf der der Behälter platziert ist  - `refWasteContainerModel`: Modell des Containers  - `regulation`: Regelung, unter der der Container betrieben wird  - `responsible`: Verantwortlich für den Behälter, d.h. Instanz, die für die Betätigung (Entleerung, Abholung, etc.) zuständig ist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `serialNumber`: Seriennummer des Containers.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `status`: Status des Containers unter dem Gesichtspunkt der Sicherheit. Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. Container ist da, wo er sein muss und steht richtig. `lidOpen`. Der Deckel des Containers wurde geöffnet und nach einer bestimmten Zeit nicht wieder geschlossen. Heruntergefallen`. Container wurde aus irgendeinem Grund fallen gelassen. verschoben`. Container wurde aus seiner regulären Position bewegt und ist nicht zurückgekommen. vandalisiert`. Der Container wurde durch Vandalismus beschädigt oder zerstört. brennend`. Container brennt und es muss eine sofortige Maßnahme ergriffen werden. Unbekannt`. Der Status des Containers ist dem System nicht bekannt.  - `storedWasteCode`: Abhängig von der Zielvorschrift. Für Europa, siehe [Europäisches Abfallverzeichnis] (http://ec.europa.eu/environment/waste/framework/list.htm).  - `storedWasteKind`: Art(en) des vom Container gelagerten Abfalls. Enum:'Organisch, anorganisch, Glas, Öl, Kunststoff, Metall, Papier, Batterien, Elektronik, Sondermüll, Sonstiges'. Oder jeder andere Wert, der nicht in den erstgenannten Bereich passt.  - `storedWasteOrigin`: Herkunft des gelagerten Abfalls. Enum:'Haushalt, Kommunal, Industrie, Bau, Gastgewerbe, Landwirtschaft, Sonstige'.  - `temperature`: Temperatur im Inneren des Behälters  - `type`: NGSI Entity Type: Es muss WasteContainer sein    
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
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
            format: uri    
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
## Beispiel-Nutzlasten  
#### WasteContainer NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WasteContainer NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WasteContainer NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### WasteContainer NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "category": [  
    "underground"  
  ],  
  "dateLastEmptying": {  
    "@type": "DateTime",  
    "@value": "2016-06-21T15:05:59.408Z"  
  },  
  "fillingLevel": 0.4,  
  "id": "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "nextActuationDeadline": "2016-06-28T15:05:59.408Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:device-Fleming:12a:1"  
  ],  
  "refWasteContainerIsle": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
  "refWasteContainerModel": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "serialNumber": "ab56kjl",  
  "status": "ok",  
  "temperature": 23,  
  "type": "WasteContainer"  
}  
```  

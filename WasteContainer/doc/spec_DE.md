<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: WasteContainer    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Abfallbehälter**    
Version: 0.3.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `RFID[string]`: Gibt die ID des RFID-Lesegeräts an  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: Stunden, die für die Betätigung über dem Behälter geeignet sind  . Model: [openingHours](openingHours)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Lande liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `annotations[array]`: Anmerkungen zum Artikel  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: Gesamtkapazität in Form des Abfallvolumens, das der Behälter aufnehmen kann  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: Farbe des Behälters. Kann zur Kennzeichnung der Abfallart verwendet werden. Die Farbcodierung sollte den Konventionen entsprechen, die für das geografische Gebiet gelten, in dem sich die Behälter befinden  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: Der Füllungsschwellenwert des Platzes, definiert als der Wert (in Prozent), bei dem die Warnung oder Benachrichtigung "Platz voll" erzeugt wird  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: Id des Abfallbehälters  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[date-time]`: Zeitpunkt, zu dem der Füllstand des Behälters zuletzt protokolliert wurde  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: Maximale Last (Gewicht), die der Abfallbehälter aufnehmen kann  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: Empfohlene Zuladung (Gewicht), die der dieser Beobachtung entsprechende Abfallbehälter aufnehmen kann  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: Gewicht der Containerladung  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Die Kategorie des Behälters. Enum:' feststehend, bodenstehend, andere, tragbar, unterirdisch'  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: Die Farbe des Produkts  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen  - `dateLastCleaning[date-time]`: Wann der Behälter das letzte Mal gereinigt wurde.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[date-time]`: Zeitstempel, der angibt, wann der Container das letzte Mal geleert wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateServiceStarted[date-time]`: Datum, an dem der Container seinen Dienst aufgenommen hat  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: Eine Beschreibung dieses Artikels  - `fillingLevel[number]`: Füllstand des Behälters  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `image[uri]`: Ein Bild des Artikels  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: Identifikator (oder Name) der Insel, auf der sich der Container befindet. Dieses Attribut sollte verwendet werden, wenn Entitäten des Typs `WasteContainerIsle` nicht speziell modelliert werden. Andernfalls sollte "refWasteContainerIsle" verwendet werden.  - `license_plate[string]`: Gibt das Nummernschild des Fahrzeugs an. SameAs: Feld "license_plate" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `methaneConcentration[number]`: Methankonzentration (CH4) im Inneren des Behälters  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `nextActuationDeadline[date-time]`: Frist für die nächste auszuführende Aktion (Entleerung, Aufnahme usw.)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[date-time]`: Deadline für die nächste Reinigung  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refDevice[array]`: Verweis auf das/die Gerät(e), das/die zur Überwachung dieses Containers verwendet wird/werden  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: Insel, auf der sich der Container befindet  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: Das Modell des Containers  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: Verordnung, unter der der Container betrieben wird  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: Verantwortlich für den Behälter, d. h. für die Betätigung (Entleerung, Abholung usw.) zuständige Stelle  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `serialNumber[string]`: Seriennummer des Behälters  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status[string]`: Status des Containers unter dem Gesichtspunkt der Sicherheit. Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. Der Container ist dort, wo er sein muss und steht ordnungsgemäß. `DeckelOffen`. Der Deckel des Behälters wurde geöffnet und nach einer bestimmten Zeit nicht wieder geschlossen. fallengelassen". Der Container wurde aus irgendeinem Grund fallen gelassen. verschoben". Der Container wurde aus seiner regulären Position verschoben und ist nicht zurückgekommen. vandalisiert". Der Container wurde durch Vandalismus beschädigt oder zerstört. brennend". Der Container brennt und es müssen sofortige Maßnahmen ergriffen werden. Unbekannt". Der Status des Containers ist dem System nicht bekannt.  - `storedWasteCode[string]`: Abhängig von der Zielvorschrift. Für Europa, siehe [Europäisches Abfallverzeichnis] (http://ec.europa.eu/environment/waste/framework/list.htm)  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: Art(en) des in dem Container gelagerten Abfalls. Enum:'organisch, anorganisch, Glas, Öl, Kunststoff, Metall, Papier, Batterien, Elektronik, gefährlich, andere'. Oder jeder andere Wert, der nicht in die erste Aufzählung passt.  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: Herkunft des gelagerten Abfalls. Enum:'Hausmüll, Siedlungsabfälle, Industrieabfälle, Bauabfälle, Gaststättenabfälle, landwirtschaftliche Abfälle, sonstige'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: Temperatur im Inneren des Behälters  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[date-time]`: Zeitstempel der Nutzdaten. Es kann Produktionsumgebungen geben, in denen der Attributtyp der Zeichenfolge "ISO8601" entspricht. In diesem Fall ist es als Synonym für "DateTime" zu betrachten. Dieses Attribut wird aus Gründen der Abwärtskompatibilität mit alten FIWARE-Referenzimplementierungen beibehalten.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI-Entitätstyp: Es muss WasteContainer sein  - `wardId[string]`: Ward Id der Entität, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WasteContainer:      
  description: A waste container      
  properties:      
    RFID:      
      description: Gives the ID of the RFID reader      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    actuationHours:      
      description: Hours suitable for performing actuations over the container      
      type: string      
      x-ngsi:      
        model: openingHours      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    annotations:      
      description: Annotations about the item      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binCapacity:      
      description: Total capacity in terms of the volume of waste the bin can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binColor:      
      description: Color of the bin. Could be used for indicating the type of waste. The color coding should follow the conventions applicable to the geographical area the bins are located      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binFullnessThreshold:      
      description: The fullness threshold level of the bin defined as the level (in terms of percentage) when the bin full alert or notification will be generated      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binId:      
      description: Id of the waste carrying bin      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binLoggedTime:      
      description: Time when the bin's level was last logged      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binMaxLoad:      
      description: Maximum load (weight) that the waste bin can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binRecommendedLoad:      
      description: Recommended load (weight) that the waste bin corresponding to this observation can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    cargoWeight:      
      description: Weight of the container load      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    category:      
      description: 'Container''s category. Enum:'' fixed, ground, other, portable, underground'''      
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
        model: https://schema.org/Text      
        type: Property      
    color:      
      description: The color of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
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
      description: Timestamp which represents when the container was emptied last time      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateServiceStarted:      
      description: Date at which the container started giving service      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    fillingLevel:      
      description: Filling level of the container      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    isleId:      
      description: 'Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used'      
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
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    methaneConcentration:      
      description: Methane (CH4) concentration inside the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nextActuationDeadline:      
      description: 'Deadline for next actuation to be performed (emptying, picking up, etc.)'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    nextCleaningDeadline:      
      description: Deadline for next cleaning      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    refDevice:      
      description: Reference to the device(s) used to monitor this container      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    refWasteContainerIsle:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Isle where the container is placed      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    refWasteContainerModel:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Container's model      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    regulation:      
      description: Regulation under which the container is operating      
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
      description: list of uri pointing to additional resources about the item      
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
      description: Serial number of the container      
      type: string      
      x-ngsi:      
        model: https://schema.org/serialNumber      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    status:      
      description: 'Container''s status from the point of view of safety. Enum:''ok , lidOpen , dropped , moved , vandalized , burning , unknown''.  -   `ok`. Container is where it must be and stands properly. `lidOpen`. Container''s lid has been opened and not closed after a certain amount of time. `dropped`. Container has been dropped for some reason. `moved`. Container has been moved from its regular position and has not come back. `vandalized`. Container has been damaged or destroyed due to vandalism. `burning`. Container is burning and an immediate action has to be taken. `unknown`. The status of the container is not known to the system'      
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
      description: 'Depend on the target regulation. For Europe, check [Europe''s List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm)'      
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
      description: Temperature inside the container      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    timeInstant:      
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations'      
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
      description: Ward Id of the entity corresponding to this observation      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Beispiel-Nutzlasten    
#### WasteContainer NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WasteContainer NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
    "type": "Number",  
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
    "type": "Number",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "Number",  
    "value": 80  
  },  
  "binRecommendedLoad": {  
    "type": "Number",  
    "value": 30  
  },  
  "binId": {  
    "type": "Text",  
    "value": "12"  
  },  
  "binMaxLoad": {  
    "type": "Number",  
    "value": 75  
  },  
  "binLoggedTime": {  
    "type": "DateTime",  
    "value": "2021-03-01T15:51:02+05:30"  
  }  
}  
```  
</details>    
#### WasteContainer NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WasteContainer NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen WasteContainer im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
    "type": "Property",  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

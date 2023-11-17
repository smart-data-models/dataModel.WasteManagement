<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Contenitore di rifiuti    
==============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un contenitore di rifiuti**    
versione: 0.3.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `RFID[string]`: Fornisce l'ID del lettore RFID  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: Ore adatte all'esecuzione di azionamenti sul contenitore  . Model: [openingHours](openingHours)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `annotations[array]`: Annotazioni sull'elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: Capacità totale in termini di volume di rifiuti che il cassonetto può contenere  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: Colore del contenitore. Può essere utilizzato per indicare il tipo di rifiuto. La codifica dei colori deve seguire le convenzioni applicabili all'area geografica in cui si trovano i cassonetti.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: Il livello di soglia di riempimento del contenitore, definito come il livello (in termini di percentuale) in cui viene generato l'avviso o la notifica di contenitore pieno.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: Id del contenitore per rifiuti  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[date-time]`: Ora in cui il livello del contenitore è stato registrato per l'ultima volta  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: Carico massimo (peso) che il cestino può contenere  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: Carico (peso) raccomandato che il contenitore dei rifiuti corrispondente a questa osservazione può contenere  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: Peso del carico del container  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Categoria del contenitore. Enum:" fisso, a terra, altro, portatile, sotterraneo".  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateLastCleaning[date-time]`: Quando il contenitore è stato pulito l'ultima volta.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[date-time]`: Timestamp che rappresenta il momento in cui il contenitore è stato svuotato l'ultima volta  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateServiceStarted[date-time]`: Data in cui il contenitore ha iniziato a fornire il servizio  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: Descrizione dell'articolo  - `fillingLevel[number]`: Livello di riempimento del contenitore  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: Identificatore (o nome) dell'isola in cui è collocato il contenitore. Questo attributo deve essere utilizzato quando le entità di tipo `WasteContainerIsle` non vengono modellate in modo specifico. Altrimenti, si dovrebbe usare `refWasteContainerIsle`.  - `license_plate[string]`: Indica il numero di targa del veicolo. Uguale a: campo 'license_plate' del messaggio in tempo reale GTFS-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `methaneConcentration[number]`: Concentrazione di metano (CH4) all'interno del contenitore  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento  - `nextActuationDeadline[date-time]`: Termine ultimo per l'esecuzione della prossima azione (svuotamento, prelievo, ecc.).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[date-time]`: Scadenza per la prossima pulizia  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refDevice[array]`: Riferimento al dispositivo o ai dispositivi utilizzati per monitorare questo contenitore.  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: Isola in cui è collocato il contenitore  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: Modello del contenitore  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: Regolamento in base al quale il contenitore opera  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: Responsabile del contenitore, vale a dire soggetto incaricato dell'azionamento (svuotamento, raccolta, ecc.)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serialNumber[string]`: Numero di serie del contenitore  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `status[string]`: Stato del contenitore dal punto di vista della sicurezza. Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. Il contenitore è dove deve essere e si trova correttamente. `CoperchioAperto`. Il coperchio del contenitore è stato aperto e non chiuso dopo un certo periodo di tempo. `gettato`. Il contenitore è caduto per qualche motivo. `mosso`. Il contenitore è stato spostato dalla sua posizione regolare e non è più tornato indietro. `vandalizzato`. Il contenitore è stato danneggiato o distrutto a causa di atti vandalici. `incendio`. Il contenitore sta bruciando e occorre intervenire immediatamente. `sconosciuto`. Lo stato del contenitore non è noto al sistema.  - `storedWasteCode[string]`: Dipende dalla normativa di riferimento. Per l'Europa, consultare [Elenco europeo dei rifiuti] (http://ec.europa.eu/environment/waste/framework/list.htm).  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: Tipo/i di rifiuti stoccati dal contenitore. Enum:'organico, inorganico, vetro, olio, plastica, metallo, carta, batterie, elettronica, pericoloso, altro'. O qualsiasi altro valore che non rientri nei precedenti.  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: Origine dei rifiuti stoccati. Enum:'domestico, urbano, industriale, edile, alberghiero, agricolo, altro'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: Temperatura all'interno del contenitore  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[date-time]`: Timestamp del payload . Possono esistere ambienti di produzione in cui il tipo di attributo è uguale alla stringa `ISO8601`. In tal caso, deve essere considerato come un sinonimo di `DateTime`. Questo attributo viene mantenuto per la compatibilità con le vecchie implementazioni di riferimento FIWARE.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: Tipo di entità NGSI: Deve essere WasteContainer  - `wardId[string]`: Ward Id dell'entità corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### Valori chiave del WasteContainer NGSI-v2 Esempio    
Ecco un esempio di WasteContainer in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Contenitore di rifiuti NGSI-v2 normalizzato Esempio    
Ecco un esempio di WasteContainer in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### Valori chiave NGSI-LD del WasteContainer Esempio    
Ecco un esempio di WasteContainer in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Contenitore di rifiuti NGSI-LD normalizzato Esempio    
Ecco un esempio di WasteContainer in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

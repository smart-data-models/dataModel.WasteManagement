<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: WasteContainerModel    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un modello di contenitore di rifiuti che cattura le proprietà statiche di una classe di contenitori **.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `alternateName[string]`: Un nome alternativo per questa voce  - `annotations[array]`: Annotazioni sull'elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nome del marchio  . Model: [https://schema.org/brand](https://schema.org/brand)- `cargoVolume[number]`: Volume totale che il contenitore può contenere  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)- `category[array]`: Categoria del contenitore. Enum:'dumpster, trashCan, wheelieBin, other'. dumpster . Vedere [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: Un elenco di norme a cui il contenitore è conforme (es. UNE-EN 840-2:2013).  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `depth[number]`: Profondità del contenitore  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Descrizione dell'articolo  - `features[array]`: Un elenco di caratteristiche del contenitore. Enum:'ruote, coperchio, coperchio arrotondato, fori di inserimento, chiusura a chiave'. Qualsiasi altro valore significativo per l'applicazione  - `height[number]`: Altezza del contenitore  . Model: [https://schema.org/heigth](https://schema.org/heigth)- `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `insertHolesNumber[number]`: Numero di fori di inserimento del contenitore  . Model: [https://schema.org/Number](https://schema.org/Number)- `madeOf[string]`: Materiale di cui è fatto il contenitore. Enum:' plastica, legno, metallo, altro '  - `madeOfCode[string]`: Codice materiale come da tabelle standard.  - `manufacturerName[string]`: Nome del produttore.  - `maximumLoad[number]`: Carico massimo che il container può contenere in sicurezza. Unità:'Chilogrammo'  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: Nome del modello fornito dal produttore. Questo attributo è diverso da name, che è solo un nome in codice solitamente fornito dai comuni.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `recommendedLoad[number]`: Carico raccomandato dal produttore per il contenitore. Unità:'Chilogrammo'  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI: Deve essere WasteContainerModel  - `weight[number]`: Peso del contenitore  . Model: [https://schema.org/weigth](https://schema.org/weigth)- `width[number]`: Larghezza del contenitore  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WasteContainerModel:      
  description: A model of waste container which captures the static properties of a class of containers.      
  properties:      
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
    brandName:      
      description: Name of the brand      
      type: string      
      x-ngsi:      
        model: https://schema.org/brand      
        type: Property      
    cargoVolume:      
      description: Total volume the container can hold      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/cargoVolume      
        type: Property      
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
      type: array      
      uniqueItems: true      
      x-ngsi:      
        type: Property      
    color:      
      description: The color of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
        type: Property      
    compliantWith:      
      description: 'A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013). '      
      items:      
        type: string      
      minItems: 0      
      type: array      
      uniqueItems: true      
      x-ngsi:      
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
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    depth:      
      description: Depth of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/depth      
        type: Property      
        units: Meters      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    features:      
      description: 'A list of container features. Enum:''wheels, lid, roundedLid, insertHoles, lockable''. Any other value meaningful for the application'      
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
      type: array      
      uniqueItems: true      
      x-ngsi:      
        type: Property      
    height:      
      description: Height of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/heigth      
        type: Property      
        units: Meters      
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
    insertHolesNumber:      
      description: Number of insert holes the container has      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    madeOf:      
      description: 'Material the container is made of. Enum:'' plastic , wood, metal, other '''      
      enum:      
        - plastic      
        - wood      
        - metal      
        - other      
      type: string      
      x-ngsi:      
        type: Property      
    madeOfCode:      
      description: 'Material Code as per standard tables. '      
      type: string      
      x-ngsi:      
        type: Property      
    manufacturerName:      
      description: 'Name of the manufacturer. '      
      type: string      
      x-ngsi:      
        type: Property      
    maximumLoad:      
      description: 'Maximum load the container can hold safely. Unit:''Kilogram'''      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    modelName:      
      description: Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
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
    recommendedLoad:      
      description: 'Manufacturer recommended load for the container. Unit:''Kilogram'''      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be WasteContainerModel'      
      enum:      
        - WasteContainerModel      
      type: string      
      x-ngsi:      
        type: Property      
    weight:      
      description: Weight of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/weigth      
        type: Property      
        units: Kilograms      
    width:      
      description: Width of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/width      
        type: Property      
        units: Meters      
  required:      
    - id      
    - type      
    - name      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainerModel/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### WasteContainerModel NGSI-v2 valori chiave Esempio    
Ecco un esempio di WasteContainerModel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "compliantWith": [  
    "UNE-EN 840-2:2013"  
  ],  
  "madeOf": "plastic",  
  "features": [  
    "wheels",  
    "lid"  
  ],  
  "category": [  
    "dumpster"  
  ]  
}  
```  
</details>    
#### WasteContainerModel NGSI-v2 normalizzato Esempio    
Ecco un esempio di WasteContainerModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "dumpster"  
    ]  
  },  
  "cargoVolume": {  
    "type": "Number",  
    "value": 150  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "C1"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "compliantWith": {  
    "type": "StructuredValue",  
    "value": [  
      "UNE-EN 840-2:2013"  
    ]  
  },  
  "madeOf": {  
    "type": "Text",  
    "value": "plastic"  
  },  
  "height": {  
    "type": "Number",  
    "value": 0.8  
  },  
  "width": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "depth": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Brute"  
  },  
  "features": {  
    "type": "StructuredValue",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  }  
}  
```  
</details>    
#### WasteContainerModel NGSI-LD valori-chiave Esempio    
Ecco un esempio di WasteContainerModel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "brandName": "Brute",  
  "cargoVolume": 150,  
  "category": [  
    "dumpster"  
  ],  
  "compliantWith": [  
    "UNE-EN 840-2:2013"  
  ],  
  "depth": 0.4,  
  "features": [  
    "wheels",  
    "lid"  
  ],  
  "height": 0.8,  
  "madeOf": "plastic",  
  "modelName": "C1",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "width": 0.5,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WasteContainerModel NGSI-LD normalizzato Esempio    
Ecco un esempio di WasteContainerModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "brandName": {  
    "type": "Property",  
    "value": "Brute"  
  },  
  "cargoVolume": {  
    "type": "Property",  
    "value": 150  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "dumpster"  
    ]  
  },  
  "compliantWith": {  
    "type": "Property",  
    "value": [  
      "UNE-EN 840-2:2013"  
    ]  
  },  
  "depth": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "features": {  
    "type": "Property",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  },  
  "height": {  
    "type": "Property",  
    "value": 0.8  
  },  
  "madeOf": {  
    "type": "Property",  
    "value": "plastic"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "C1"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "width": {  
    "type": "Property",  
    "value": 0.5  
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

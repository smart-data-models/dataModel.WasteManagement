<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: WasteContainerModel    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Modell des Abfallbehälters, das die statischen Eigenschaften einer Klasse von Behältern erfasst.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `annotations[array]`: Anmerkungen zum Artikel  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Name der Marke  . Model: [https://schema.org/brand](https://schema.org/brand)- `cargoVolume[number]`: Gesamtvolumen, das der Behälter fassen kann  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)- `category[array]`: Die Kategorie des Containers. Enum:'dumpster, trashCan, wheelieBin, other'. dumpster . Siehe [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color[string]`: Die Farbe des Produkts  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: Eine Liste der Normen, denen der Behälter entspricht (z. B. UNE-EN 840-2:2013).  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `depth[number]`: Tiefe des Behälters  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Eine Beschreibung dieses Artikels  - `features[array]`: Eine Liste von Containereigenschaften. Enum:'Räder, Deckel, roundedLid, insertHoles, verschließbar'. Jeder andere für die Anwendung sinnvolle Wert  - `height[number]`: Höhe des Behälters  . Model: [https://schema.org/heigth](https://schema.org/heigth)- `id[*]`: Eindeutiger Bezeichner der Entität  - `image[uri]`: Ein Bild des Artikels  . Model: [https://schema.org/URL](https://schema.org/URL)- `insertHolesNumber[number]`: Anzahl der Einstecklöcher, die der Behälter hat  . Model: [https://schema.org/Number](https://schema.org/Number)- `madeOf[string]`: Material, aus dem der Behälter hergestellt ist. Enum:' Kunststoff, Holz, Metall, andere '  - `madeOfCode[string]`: Materialcode gemäß den Standardtabellen.  - `manufacturerName[string]`: Name des Herstellers.  - `maximumLoad[number]`: Maximale Ladung, die der Container sicher aufnehmen kann. Einheit:'Kilogramm'  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: Name des Modells, wie vom Hersteller angegeben. Dieses Attribut unterscheidet sich von Name, der nur ein Codename ist, der normalerweise von den Gemeinden vergeben wird  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `recommendedLoad[number]`: Vom Hersteller empfohlene Beladung für den Container. Einheit:'Kilogramm'  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Entitätstyp: Es muss WasteContainerModel sein  - `weight[number]`: Gewicht des Containers  . Model: [https://schema.org/weigth](https://schema.org/weigth)- `width[number]`: Breite des Containers  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### WasteContainerModel NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WasteContainerModel NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WasteContainerModel NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WasteContainerModel NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

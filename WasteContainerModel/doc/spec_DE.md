Entität: WasteContainerModel  
============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)  
Globale Beschreibung: **Ein Modell des Abfallbehälters, das die statischen Eigenschaften einer Klasse von Behältern erfasst.**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `brandName`: Name der Marke  - `cargoVolume`: Gesamtvolumen, das der Behälter aufnehmen kann  - `category`: Die Kategorie des Containers. Enum:'dumpster, trashCan, wheelieBin, other'. dumpster . Siehe [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color`: Die Farbe des Produkts  - `compliantWith`: Eine Liste der Normen, denen der Behälter entspricht (z. B. UNE-EN 840-2:2013).  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `depth`: Tiefe des Behälters  - `description`: Eine Beschreibung dieses Artikels  - `features`: Eine Liste von Containereigenschaften. Enum:'wheels, lid, roundedLid, insertHoles, lockable'. Jeder andere für die Anwendung sinnvolle Wert.  - `height`: Höhe des Behälters  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `insertHolesNumber`: Anzahl der Einsatzlöcher, die der Behälter hat  - `madeOf`: Material, aus dem der Behälter besteht. Enum:' Kunststoff, Holz, Metall, andere '  - `madeOfCode`: Material Code gemäß Standardtabellen.  - `manufacturerName`: Name des Herstellers.  - `maximumLoad`: Maximale Last, die der Container sicher aufnehmen kann. Einheit:'Kilogramm'  - `modelName`: Name des Modells, wie vom Hersteller angegeben. Dieses Attribut unterscheidet sich von Name, der nur ein Codename ist, der normalerweise von Gemeinden vergeben wird.  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `recommendedLoad`: Vom Hersteller empfohlene Last für den Container. Einheit:'Kilogramm'  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI-Entitätstyp: Es muss WasteContainerModel sein  - `weight`: Gewicht des Behälters  - `width`: Breite des Containers    
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### WasteContainerModel NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WasteContainerModel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WasteContainerModel NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### WasteContainerModel NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein WasteContainerModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "madeOf": "plastic",  
  "modelName": "C1",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "type": "WasteContainerModel",  
  "width": 0.5  
}  
```  

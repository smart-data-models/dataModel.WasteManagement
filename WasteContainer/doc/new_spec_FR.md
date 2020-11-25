Entité : WasteContainer  
=======================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Un conteneur de déchets**  

## Liste des biens  

- `TimeInstant`:   - `actuationHours`:   - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`:   - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `cargoWeight`:   - `category`:   - `color`: La couleur du produit.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateLastCleaning`:   - `dateLastEmptying`:   - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateServiceStarted`:   - `description`: Une description de cet article  - `fillingLevel`:   - `id`:   - `image`: Une image de l'objet.  - `isleId`:   - `location`:   - `methaneConcentration`:   - `name`: Le nom de cet article.  - `nextActuationDeadline`:   - `nextCleaningDeadline`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refDevice`:   - `refWasteContainerIsle`:   - `refWasteContainerModel`:   - `regulation`:   - `responsible`:   - `seeAlso`:   - `serialNumber`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`:   - `storedWasteCode`:   - `storedWasteKind`:   - `storedWasteOrigin`:   - `temperature`:   - `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
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
</details>    
## Exemples de charges utiles  
#### Conteneur de déchets NGSI V2 valeurs clés Exemple  
Voici un exemple de conteneur de déchets au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Conteneur de déchets NGSI V2 normalisé Exemple  
Voici un exemple de conteneur de déchets au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Conteneur à déchets Valeurs clés de l'INSG-LD Exemple  
Voici un exemple de conteneur de déchets au format JSON-LD en tant que valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Conteneur de déchets NGSI-LD normalisé Exemple  
Voici un exemple de conteneur de déchets au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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

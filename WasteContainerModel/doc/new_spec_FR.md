Entité : WasteContainerModel  
============================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Un modèle de conteneur de déchets**  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `annotations`:   - `brandName`:   - `cargoVolume`:   - `category`:   - `color`: La couleur du produit.  - `compliantWith`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `depth`:   - `description`: Une description de cet article  - `features`:   - `height`:   - `id`:   - `image`: Une image de l'objet.  - `insertHolesNumber`:   - `madeOf`:   - `madeOfCode`:   - `manufacturerName`:   - `maximumLoad`:   - `modelName`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `recommendedLoad`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: NGSI Type d'entité  - `weight`:   - `width`:   ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerModel:    
  description: 'A waste container model'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    brandName:    
      type: string    
    cargoVolume:    
      minimum: 0    
      type: number    
    category:    
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
    color:    
      description: 'The color of the product.'    
      type: string    
    compliantWith:    
      items:    
        type: string    
      minItems: 0    
      type: array    
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
      minimum: 0    
      type: number    
    description:    
      description: 'A description of this item'    
      type: Property    
    features:    
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
    height:    
      minimum: 0    
      type: number    
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
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    insertHolesNumber:    
      minimum: 0    
      type: number    
    madeOf:    
      enum:    
        - plastic    
        - wood    
        - metal    
        - other    
      type: string    
    madeOfCode:    
      type: string    
    manufacturerName:    
      type: string    
    maximumLoad:    
      minimum: 0    
      type: number    
    modelName:    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    recommendedLoad:    
      minimum: 0    
      type: number    
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
        - WasteContainerModel    
      type: string    
    weight:    
      minimum: 0    
      type: number    
    width:    
      minimum: 0    
      type: number    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WasteContainerModel NGSI V2 key-values Example  
Voici un exemple de modèle de conteneur de déchets au format JSON comme valeurs clés. Ce modèle est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### WasteContainerModel NGSI V2 normalisé Exemple  
Voici un exemple de WasteContainerModel au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### WasteContainerModel NGSI-LD key-values Example  
Voici un exemple de modèle de conteneur de déchets au format JSON-LD comme valeurs clés. Ce modèle est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Brute",  
 "cargoVolume": 150,  
 "category": ["dumpster"],  
 "compliantWith": ["UNE-EN 840-2:2013"],  
 "depth": 0.4,  
 "features": ["wheels", "lid"],  
 "height": 0.8,  
 "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
 "madeOf": "plastic",  
 "modelName": "C1",  
 "name": "Dumpster_Brute_2009_Plastic_Green",  
 "type": "WasteContainerModel",  
 "width": 0.5}  
```  
#### WasteContainerModel NGSI-LD normalisé Exemple  
Voici un exemple de WasteContainerModel au format JSON-LD tel que normalisé. Ce modèle est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  

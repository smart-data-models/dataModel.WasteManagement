Entité : WasteContainer  
=======================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Un conteneur à déchets**  
version : 0.3.0  

## Liste des propriétés  

- `RFID`: Donne l'ID du lecteur RFID.  - `actuationHours`: Heures appropriées pour effectuer des actions sur le conteneur.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `annotations`: Annotations sur l'élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `binCapacity`: Capacité totale en termes de volume de déchets que la poubelle peut contenir.  - `binColor`: Couleur de la poubelle. Peut être utilisée pour indiquer le type de déchets. Le code couleur doit respecter les conventions applicables à la zone géographique où se trouvent les poubelles.  - `binFullnessThreshold`: Le niveau du seuil de remplissage du bac défini comme le niveau (en termes de pourcentage) auquel l'alerte ou la notification de bac plein sera générée.  - `binId`: Id de la poubelle  - `binLoggedTime`: Heure à laquelle le niveau de l'emplacement a été enregistré pour la dernière fois.  - `binMaxLoad`: Charge (poids) maximale que peut supporter la poubelle.  - `binRecommendedLoad`: Charge (poids) recommandée que peut contenir la poubelle correspondant à cette observation.  - `cargoWeight`: Poids du chargement du conteneur.  - `category`: Enum:' fixe, terrestre, autre, portable, souterrain'.  - `color`: La couleur du produit  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastCleaning`: Quand le conteneur a été nettoyé la dernière fois.  - `dateLastEmptying`: Horodatage qui représente la dernière fois que le conteneur a été vidé.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateServiceStarted`: Date à laquelle le conteneur a commencé à rendre service.  - `description`: Une description de cet article  - `fillingLevel`: Niveau de remplissage du conteneur  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'article  - `isleId`: Identificateur (ou nom) de l'île où le conteneur est placé. Cet attribut doit être utilisé lorsque des entités de type `WasteContainerIsle` ne sont pas modélisées spécifiquement. Sinon, il faut utiliser `refWasteContainerIsle`.  - `license_plate`: Donne le numéro de la plaque d'immatriculation du véhicule. Identique à : Champ 'license_plate' du GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `methaneConcentration`: Concentration de méthane (CH4) à l'intérieur du conteneur.  - `name`: Le nom de cet élément.  - `nextActuationDeadline`: Heure limite pour l'exécution de la prochaine action (vidage, ramassage, etc.).  - `nextCleaningDeadline`: Date limite pour le prochain nettoyage.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refDevice`: Référence au(x) dispositif(s) utilisé(s) pour surveiller ce conteneur  - `refWasteContainerIsle`: Est où le conteneur est placé  - `refWasteContainerModel`: Modèle de conteneur  - `regulation`: Règlement sous lequel le conteneur est exploité  - `responsible`: Responsable du conteneur, c'est-à-dire entité chargée de l'actionner (vidange, collecte, etc.)  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `serialNumber`: Numéro de série du conteneur.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status`: Statut du conteneur du point de vue de la sécurité. Enum : 'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. Le conteneur est là où il doit être et se tient correctement. `lidOpen`. Le couvercle du conteneur a été ouvert et n'a pas été refermé après un certain temps. `dropped`. Le conteneur est tombé pour une raison quelconque. `moved`. Le conteneur a été déplacé de sa position normale et n'est pas revenu. `vandalisé`. Le conteneur a été endommagé ou détruit à cause d'un acte de vandalisme. `brûlé`. Le conteneur brûle et une action immédiate doit être prise. `inconnu`. L'état du conteneur n'est pas connu du système.  - `storedWasteCode`: Cela dépend de la réglementation visée. Pour l'Europe, consultez la [Liste européenne des déchets] (http://ec.europa.eu/environment/waste/framework/list.htm).  - `storedWasteKind`: Type(s) de déchets stockés par le conteneur. Enum : "organique, inorganique, verre, huile, plastique, métal, papier, batteries, électronique, dangereux, autre". Ou toute autre valeur qui ne correspond pas à la première.  - `storedWasteOrigin`: Origine des déchets stockés. Enum : "ménage, municipal, industriel, construction, hôtellerie, agriculture, autre".  - `temperature`: Température à l'intérieur du conteneur  - `timeInstant`: Horodatage de la charge utile. Il peut y avoir des environnements de production où le type d'attribut est égal à la chaîne `ISO8601`. Dans ce cas, il doit être considéré comme un synonyme de `DateTime`. Cet attribut est conservé pour des raisons de rétrocompatibilité avec les anciennes implémentations de la référence FIWARE.  - `type`: Type d'entité NGSI : Il doit s'agir de WasteContainer  - `wardId`: Ward Id de l'entité correspondant à cette observation.    
Propriétés requises  
- `id`  - `location`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      x-ngsi:    
        type: Geoproperty    
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
  version: 0.3.0    
```  
</details>    
## Exemples de charges utiles  
#### WasteContainer NGSI-v2 valeurs-clés Exemple  
Voici un exemple de WasteContainer au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### WasteContainer NGSI-v2 normalisé Exemple  
Voici un exemple de WasteContainer au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Valeurs-clés NGSI-LD du WasteContainer Exemple  
Voici un exemple de WasteContainer au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "@context": [  
    "iudx:WmgmtBin",  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
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
#### WasteContainer NGSI-LD normalisé Exemple  
Voici un exemple de WasteContainer au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ],  
      "type": "Point"  
    }  
  },  
  "binCapacity": {  
    "type": "Property",  
    "value": 43  
  },  
  "binColor": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "binClearedTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "21"  
  },  
  "binCategory": {  
    "type": "Property",  
    "value": "Household Bin"  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA23F2345"  
  },  
  "RFID": {  
    "type": "Property",  
    "value": "67855734"  
  },  
  "binFillingLevel": {  
    "type": "Property",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "Property",  
    "value": 80  
  },  
  "binRecommendedLoad": {  
    "type": "Property",  
    "value": 30  
  },  
  "binId": {  
    "type": "Property",  
    "value": "12"  
  },  
  "binMaxLoad": {  
    "type": "Property",  
    "value": 75  
  },  
  "binLoggedTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "@context": [  
    "iudx:WmgmtBin",  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude
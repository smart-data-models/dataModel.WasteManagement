<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WasteContainer  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un conteneur à déchets**  
version : 0.3.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `RFID[string]`: Donne l'ID du lecteur RFID.  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: Heures appropriées pour effectuer des actions sur le conteneur.  . Model: [openingHours](openingHours)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `annotations[array]`: Annotations sur l'élément  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: Capacité totale en termes de volume de déchets que la poubelle peut contenir.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: Couleur de la poubelle. Peut être utilisée pour indiquer le type de déchets. Le code couleur doit respecter les conventions applicables à la zone géographique où se trouvent les poubelles.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: Le niveau du seuil de remplissage du bac défini comme le niveau (en termes de pourcentage) auquel l'alerte ou la notification de bac plein sera générée.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: Id de la poubelle  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[string]`: Heure à laquelle le niveau de l'emplacement a été enregistré pour la dernière fois.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: Charge (poids) maximale que peut supporter la poubelle.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: Charge (poids) recommandée que peut contenir la poubelle correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: Poids du chargement du conteneur.  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Enum:' fixe, terrestre, autre, portable, souterrain'.  . Model: [https://schema.org/Text Containers category](https://schema.org/Text Containers category)- `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastCleaning[string]`: Quand le conteneur a été nettoyé la dernière fois.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[string]`: Horodatage qui représente la dernière fois que le conteneur a été vidé.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateServiceStarted[string]`: Date à laquelle le conteneur a commencé à rendre service.  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: Une description de cet article  - `fillingLevel[number]`: Niveau de remplissage du conteneur  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `image[string]`: Une image de l'article  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: Identificateur (ou nom) de l'île où le conteneur est placé. Cet attribut doit être utilisé lorsque des entités de type `WasteContainerIsle` ne sont pas modélisées spécifiquement. Sinon, il faut utiliser `refWasteContainerIsle`.  - `license_plate[string]`: Donne le numéro de la plaque d'immatriculation du véhicule. Identique à : Champ 'license_plate' du GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `methaneConcentration[number]`: Concentration de méthane (CH4) à l'intérieur du conteneur.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément.  - `nextActuationDeadline[string]`: Heure limite pour l'exécution de la prochaine action (vidage, ramassage, etc.).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[string]`: Date limite pour le prochain nettoyage.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refDevice[array]`: Référence au(x) dispositif(s) utilisé(s) pour surveiller ce conteneur  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: Est où le conteneur est placé  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: Modèle de conteneur  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: Règlement sous lequel le conteneur est exploité  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: Responsable du conteneur, c'est-à-dire entité chargée de l'actionner (vidange, collecte, etc.)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `serialNumber[string]`: Numéro de série du conteneur.  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status[string]`: Statut du conteneur du point de vue de la sécurité. Enum : 'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok`. Le conteneur est là où il doit être et se tient correctement. `lidOpen`. Le couvercle du conteneur a été ouvert et n'a pas été refermé après un certain temps. `dropped`. Le conteneur est tombé pour une raison quelconque. `moved`. Le conteneur a été déplacé de sa position normale et n'est pas revenu. `vandalisé`. Le conteneur a été endommagé ou détruit à cause d'un acte de vandalisme. `brûlé`. Le conteneur brûle et une action immédiate doit être prise. `inconnu`. L'état du conteneur n'est pas connu du système.  - `storedWasteCode[string]`: Cela dépend de la réglementation visée. Pour l'Europe, consultez la [Liste européenne des déchets] (http://ec.europa.eu/environment/waste/framework/list.htm).  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: Type(s) de déchets stockés par le conteneur. Enum : "organique, inorganique, verre, huile, plastique, métal, papier, batteries, électronique, dangereux, autre". Ou toute autre valeur qui ne correspond pas à la première.  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: Origine des déchets stockés. Enum : "ménage, municipal, industriel, construction, hôtellerie, agriculture, autre".  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: Température à l'intérieur du conteneur  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[string]`: Horodatage de la charge utile. Il peut y avoir des environnements de production où le type d'attribut est égal à la chaîne `ISO8601`. Dans ce cas, il doit être considéré comme un synonyme de `DateTime`. Cet attribut est conservé pour des raisons de rétrocompatibilité avec les anciennes implémentations de la référence FIWARE.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: Type d'entité NGSI : Il doit s'agir de WasteContainer  - `wardId[string]`: Ward Id de l'entité correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### WasteContainer NGSI-v2 valeurs-clés Exemple  
Voici un exemple de WasteContainer au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### WasteContainer NGSI-v2 normalisé Exemple  
Voici un exemple de WasteContainer au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Conteneur à déchets Valeurs-clés NGSI-LD Exemple  
Voici un exemple de WasteContainer au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### WasteContainer NGSI-LD normalisé Exemple  
Voici un exemple de WasteContainer au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

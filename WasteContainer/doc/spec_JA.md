エンティティウェストコンテナ  
==============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明。**ゴミ箱  

## プロパティのリスト  

- `RFID`: RFIDリーダーのIDを示す。  - `actuationHours`: 容器の上で動作を行うのに適した時間。  - `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `annotations`: アイテムに関するアノテーション  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `binCapacity`: ビンが収容できるゴミの量を示す総容量。  - `binColor`: ビンの色。廃棄物の種類を示すために使用される可能性がある。色分けは、ビンが設置されている地理的エリアに適用される慣例に従うべきである。  - `binFullnessThreshold`: ビンの満杯しきい値は、ビンが満杯になったときにアラートや通知が発生するレベル（パーセンテージ）として定義されます。  - `binId`: 廃棄物運搬用ビンの形状  - `binLoggedTime`: ビンのレベルが最後にログに記録された時間。  - `binMaxLoad`: ゴミ箱が保持できる最大荷重（重量）。  - `binRecommendedLoad`: この観測に対応するゴミ箱が保持できる推奨荷重（重量）。  - `cargoWeight`: コンテナロードの重量  - `category`: Enum:'固定、地面、その他、ポータブル、地下'  - `color`: 商品の色について  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastCleaning`: 前回、容器を洗浄したとき。  - `dateLastEmptying`: コンテナが最後に空になった時刻を示すタイムスタンプ。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateServiceStarted`: コンテナがサービスを開始した日。  - `description`: このアイテムの説明  - `fillingLevel`: 容器の充填レベル  - `id`: エンティティのユニークな識別子  - `image`: アイテムのイメージ  - `isleId`: コンテナが置かれているアイルの識別子（または名前）です。この属性は、`WasteContainerIsle`タイプのエンティティが具体的にモデル化されていない場合に使用する必要があります。そうでない場合は、`refWasteContainerIsle` を使用してください。  - `license_plate`: 車両のライセンスプレート番号を示す。SameAs:GTFS Realtime message-VehicleDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）の「license_plate」フィールド。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `methaneConcentration`: 容器内のメタン（CH4）濃度。  - `name`: このアイテムの名前です。  - `nextActuationDeadline`: 次のアクチュエーション（空にする、拾うなど）を実行するための期限。  - `nextCleaningDeadline`: 次回のクリーニングの締め切り  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `refDevice`: このコンテナをモニターするために使用されるデバイスの参照先  - `refWasteContainerIsle`: コンテナが置かれているアイル  - `refWasteContainerModel`: コンテナのモデル  - `regulation`: コンテナが運用されている規制  - `responsible`: 容器の責任者、すなわち作動（空にする、回収するなど）を担当する団体  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `serialNumber`: コンテナのシリアルナンバー。  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `status`: 安全性の観点から見たコンテナの状態を示す。Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  - `ok` です。コンテナはあるべき場所にあり、きちんと立っています。`lidOpen`.コンテナの蓋が開かれ、一定の時間が経過しても閉まらない。`dropped`.コンテナが何らかの理由で落とされた。移動した``。コンテナが定位置から移動されて、戻ってこない。`破壊された`.コンテナが破壊行為によって、破損したり破壊されたりした。`燃えている`.コンテナが燃えているので、早急に対処する必要があります。`unknown`.コンテナの状態はシステムに知らされていません。  - `storedWasteCode`: 対象となる規制による。欧州の場合は、[欧州の廃棄物リスト](http://ec.europa.eu/environment/waste/framework/list.htm)をご確認ください。  - `storedWasteKind`: コンテナに保管されている廃棄物の種類/s。Enum:'organic, inorganic, glass, oil, plastic, metal, paper, batteries, electronics, hazardous, other'.または、前者に当てはまらないその他の値。  - `storedWasteOrigin`: 保管されている廃棄物の起源。Enum:'home, municipal, industrial, construction, hostelry, agriculture, other'.  - `temperature`: 容器内の温度  - `timeInstant`: ペイロードのタイムスタンプ。本番環境では、属性タイプが `ISO8601` の文字列と同じである場合があります。その場合は、`DateTime` の同義語として考えなければなりません。この属性は、古いFIWAREリファレンスの実装との下位互換性のために残されています。  - `type`: NGSI Entity Typeです。WasteContainerでなければならない。  - `wardId`: Ward この観測に対応するエンティティのId。    
必須項目  
- `id`  - `location`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainer/schema.json    
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
## ペイロードの例  
#### WasteContainer NGSI-v2 キーバリューの例  
ここでは、WasteContainerをJSON-LD形式でkey-valuesにした例を紹介します。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WasteContainer NGSI-v2 正規化された例。  
ここでは、正規化されたJSON-LD形式のWasteContainerの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WasteContainer NGSI-LDのキーバリューの例。  
ここでは、WasteContainerをJSON-LD形式でkey-valuesにした例を紹介します。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WasteContainer NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のWasteContainerの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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

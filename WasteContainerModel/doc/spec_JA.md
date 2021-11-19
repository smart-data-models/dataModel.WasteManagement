エンティティ。WasteContainerModel  
==========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**廃棄物処理容器のモデルで、容器のクラスの静的な特性を表現しています。  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `annotations`: アイテムに関するアノテーション  - `brandName`: ブランド名  - `cargoVolume`: 容器に入れられる総量  - `category`: コンテナのカテゴリ。Enum:'dumpster, trashCan, wheelieBin, other'. ダンプスター .https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)参照  - `color`: 商品の色について  - `compliantWith`: 容器が準拠している規格のリスト（例：UNE-EN 840-2:2013）。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `depth`: 容器の深さ  - `description`: このアイテムの説明  - `features`: コンテナの機能のリストです。Enum:'wheel, lid, roundedLid, insertHoles, lockable'.その他、用途に応じて意味のある値を指定します。  - `height`: コンテナの高さ  - `id`: エンティティのユニークな識別子  - `image`: アイテムのイメージ  - `insertHolesNumber`: 容器にある挿入口の数  - `madeOf`: コンテナの材質。Enum:' プラスチック , 木材 , 金属 , その他 '  - `madeOfCode`: 材料コードは標準的な表の通りです。  - `manufacturerName`: メーカー名です。  - `maximumLoad`: コンテナが安全に保持できる最大荷重。単位:'キログラム'  - `modelName`: 製造者によって与えられたモデルの名前。この属性は、通常自治体で与えられる単なるコードネームであるnameとは異なります。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `recommendedLoad`: コンテナのメーカー推奨荷重。単位:'キログラム'  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity Typeです。WasteContainerModelでなければならない。  - `weight`: コンテナの重量  - `width`: コンテナの幅    
必須項目  
- `id`  - `name`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerModel:    
  description: 'A model of waste container which captures the static properties of a class of containers.'    
  properties:    
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
    brandName:    
      description: 'Name of the brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cargoVolume:    
      description: 'Total volume the container can hold'    
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
      description: 'The color of the product'    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    depth:    
      description: 'Depth of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
        units: Meters    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    height:    
      description: 'Height of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/heigth    
        type: Property    
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
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    insertHolesNumber:    
      description: 'Number of insert holes the container has'    
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
      description: 'Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities.'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'Weight of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weigth    
        type: Property    
        units: Kilograms    
    width:    
      description: 'Width of the container'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainerModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### WasteContainerModel NGSI-v2 key-valuesの例。  
ここでは、WasteContainerModelをJSON-LD形式でkey-valuesにした例を紹介します。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WasteContainerModel NGSI-v2 正規化された例。  
ここでは、正規化されたJSON-LD形式のWasteContainerModelの例を示します。これはオプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "type": "array",  
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
    "type": "array>",  
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
    "type": "array",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  }  
}  
```  
#### WasteContainerModel NGSI-LDのキーバリューの例  
ここでは、WasteContainerModelをJSON-LD形式でkey-valuesにした例を紹介します。これは`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WasteContainerModel NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のWasteContainerModelの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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

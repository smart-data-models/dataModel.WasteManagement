[![Status badge](https://img.shields.io/badge/status-draft-red.svg)](RELEASE_NOTES)
[![Build badge](https://img.shields.io/travis/smart-data-models/dataModel.WasteManagement.svg "Travis build status")](https://travis-ci.org/smart-data-models/dataModel.WasteManagement/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
# Waste Management Harmonized Data Models

These data models describe the main entities that are typically involved in
waste management scenarios. In fact, these models have been devised to be as
generic as possible, thus allowing to deal with different scenarios:

-   Municipal waste management with on street / buried containers.
-   Industrial waste management using specialized containers.
-   Containers used occasionally on street (construction waste containers, etc.)
-   Litters placed on street or public places where waste is left by the public.

The main entities identified are:

-   [`WasteContainerIsle`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainerIsle/swagger.yaml) . Isle which holds
    one or more containers. On a municipal scenario they are delimited on street
    areas.
-   [`WasteContainerModel`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainerModel/swagger.yaml) . It represents a
    model of waste container, capturing its static properties such as
    dimensions, materials or features.
-   [`WasteContainer`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainer/swagger.yaml) . It represents a particular
    instance of waste container placed at a particular isle or place. All the
    dynamic properties of a container, for instance, `fillingLevel` are included
    by this entity.
-   `LitterModel`. It is a model of litter, including all its static properties.
    (T.B.D.)
-   `Litter`. It represents a particular instance of litter. (T.B.D.)

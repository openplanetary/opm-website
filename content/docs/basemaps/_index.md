---
title: 'Basemaps'
weight: 2
loadLeafletResources: true
---

We are designing and making accessible a collection of basemaps that can be used for the development of planetary web mapping applications. All our basemaps are currently XYZ-based Web Mercator projected tiles that can be fetched using web clients such as Leaflet or OpenLayers.

## Interactive map examples

Below is an example of an interactive map using our new `leaflet-map` Hugo shortcode:

```
{{</* leaflet-map
  layer_url="https://cartocdn-gusc.global.ssl.fastly.net/opmbuilder/api/v1/map/named/opm-mars-basemap-v0-2/all/{z}/{x}/{y}.png"
  height="400px"
  width="100%"
  tms="false"
  map_id="map1"
*/>}}
```

{{< leaflet-map layer_url="https://cartocdn-gusc.global.ssl.fastly.net/opmbuilder/api/v1/map/named/opm-mars-basemap-v0-2/all/{z}/{x}/{y}.png" height="400px" width="100%" tms="false" map_id="map1" >}}

Here is another one:

{{< leaflet-map layer_url="http://s3-eu-west-1.amazonaws.com/whereonmars.cartodb.net/mola_color-noshade_global/{z}/{x}/{y}.png" height="400px" width="100%" tms="true" map_id="map2" >}}

---
date: '2025-07-04T15:33:12+02:00'
draft: false
title: 'Home'
layout: hextra-home
---

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Build beautiful web interactive maps of planetary bodies
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  OpenPlanetaryMap is a community project to enable space enthusiasts and students, planetary researchers and mappers, educators and storytellers to easily and collaboratively create and share location-based knowledge and maps of planets and planetary bodies.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-button text="Browse Basemaps" link="basemaps" >}}
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Datasets"
    icon="database"
    subtitle="We curate an open repository of datasets related to planetary geography, topography, geology, weather, climate, scientific missions and discoveries, robotic and human exploration."
    link="/datasets"
  >}}
  {{< hextra/feature-card
    title="Basemaps"
    icon="map"
    subtitle="We design and implement beautifully crafted vector-based basemaps of planetary bodies that can serve as base layer for your web mapping applications and visualisations."
    link="/basemaps"
  >}}
  {{< hextra/feature-card
    title=""
    icon=""
    subtitle="We also intend to develop geocoding and georeferencing APIs that will make it easy to discover, search, share, discuss and crowdsource datasets of places on Mars, the Moon and other planetary bodies."
    link="/places"
  >}}
{{< /hextra/feature-grid >}}

<div class="hx:mt-4"></div>

<div class="hx:w-full hx:flex hx:flex-col hx:items-center hx:mt-6 hx:mb-6">

<div class="hx:text-lg">
{{< hextra/hero-section >}}
Showcase
{{< /hextra/hero-section >}}
</div>

<p class="hx:mt-1 hx:mb-4 hx:text-center hx:text-lg hx:text-gray-500 hx:dark:text-gray-400">
Web map interfaces using OPM basemaps.
</p>

</div>

{{< cards >}}
  {{< card
        link="https://psa.esa.int"
        title="ESA's Planetary Science Archive (PSA)"
        subtitle="Web interface for accessing raw, calibrated, and derived data from the European Space Agency’s planetary missions."
        image="images/esa_psa.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

  {{< card
        link="https://pdssp.ias.universite-paris-saclay.fr"
        title="Pôle de Données et Services Surfaces Planétaires (PDSSP)"
        subtitle="Web interface for accessing, visualising, and analysing planetary science data distributed across French's laboratories."
        image="images/pdssp.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

  {{< card
        link="https://observations.cassis.unibe.ch/"
        title="TGO/CaSSIS Observations"
        subtitle="Web interface for accessing the ESA's Trace Gas Orbiter CaSSIS instrument observational data."
        image="images/cassis_observations.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

  {{< card
        link="https://explore-platform.eu/space-browser"
        title="EXPLORE Space Browser"
        subtitle="Web interface for accessing planetary data from Mars, Moon, and Mercury."
        image="images/explore_space_browser.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

  {{< card
        link="https://geosketch.io/moon/"
        title="Geosketch Moon"
        subtitle="Web interface for collaborative sharing of geospatial snippets via Qgis WKT copy-paste."
        image="images/geosketch_moon.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

  {{< card
        link="https://muted.uni-muenster.de"
        title="Multi-temporal Database of Planetary Image Data (MUTED)"
        subtitle="Web interface to identify the spatial and temporal coverage of planetary image data from Mars, Moon, and Mercury."
        image="images/muted.png"
        imageStyle="object-fit:cover; aspect-ratio:16/9;"
  >}}

{{< /cards >}}

<div class="hx:mt-4"></div>


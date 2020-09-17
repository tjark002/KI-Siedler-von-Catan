//Siedlungen muessen zwei Strassen von der naechsten entfernt werden, die zu nahen Bauplaetze werden zerstoert
if (buildVillage != null)
{
    GameObject cityPlaceInstance = Instantiate(cityPlace);

    cityPlaceInstance.transform.position = buildVillage.transform.position;
    cityPlaceInstance.GetComponent<BuildCity>().player = activePlayer;
    cityPlaceInstance.GetComponent<BuildCity>().gameManager = this;
    cityPlaceInstance.GetComponent<BuildCity>().row = tempRow;
    cityPlaceInstance.GetComponent<BuildCity>().column = tempColumn;
    cityPlaceInstance.GetComponent<BuildCity>().UpdatePositionForAI();
    cityPlaceInstance.GetComponent<BuildCity>().tiles = new List<GameObject>(buildVillage.GetComponent<Village>().tiles);

    cityPlaceInstances.Add(cityPlaceInstance);
    map.cityBuildPlaces.Add(cityPlaceInstance.GetComponent<BuildCity>().cityPlace);

    DestroyVillagePlacesInRadius();
    buildVillage = null;
}
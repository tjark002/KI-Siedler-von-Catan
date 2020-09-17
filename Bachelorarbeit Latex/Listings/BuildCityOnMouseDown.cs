private void OnMouseDown()
{
    cityPlace.row = row;
    cityPlace.column = column;
    //Liefert nur eine Siedlung zurueck, wenn die Bedingungen für den Spieler erfuellt sind
    GameObject cityInstance = player.BuildCity(this.transform.position);

    //Die Informationen über anliegende Ressourcenfelder werden aus dem Bauplatz auf die Siedlung übertragen
    City cityScript = cityInstance.GetComponent<City>();
    cityScript.tiles = new List<GameObject>(this.tiles);

    player.cities.Add(cityInstance);

    gameManager.cityPlaceInstances.Remove(this.gameObject);
    gameManager.map.cityBuildPlaces.Remove(cityPlace);
    Destroy(this.gameObject);
    cityPlace = null;
}
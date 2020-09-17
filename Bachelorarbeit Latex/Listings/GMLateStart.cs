private void LateStart()
{
    //Die Karte kann erst jetzt geholt werden, da sie vorher noch nicht fertig war.
    map = mapGenerator.map;

    Transform transform = villagePlaces.GetComponent<Transform>();
    for (int i = villagePlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
    {
        Transform child = transform.GetChild(i);
        map.villageBuildPlaces.Add(child.gameObject.GetComponent<buildVillage>().villagePlace);
    }

    transform = roadPlaces.GetComponent<Transform>();
    for (int i = roadPlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
    {
        Transform child = transform.GetChild(i);
        map.roadBuildPlaces.Add(child.gameObject.GetComponent<BuildRoad>().roadPlace);
    }

    //Nun kann der erste Zug von Spieler 1 ausgeführt werden
    activePlayer.FirstTurn();
    StartAIProcess();
    MakeAiTurn(4f);
}
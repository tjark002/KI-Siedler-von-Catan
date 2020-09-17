void Update()
{
    if (villageFocus.hasFocus && (activePlayer.isFirstTurn || activePlayer.isSecondTurn))
    {
        villagePlaces.SetActive(true);
        Transform transform = villagePlaces.GetComponent<Transform>();
        for (int i = villagePlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
        {
            Transform child = transform.GetChild(i);
            child.gameObject.SetActive(true);
        }
        if (buildVillage != null)
        {
            DestroyVillagePlacesInRadius();
        }

    } 
	...//Äuqivalent mit HasResourcesForVillage statt isFirstTurn und is SecondTurn
    else
    {
        Transform transform = villagePlaces.GetComponent<Transform>();
        for (int i = villagePlaces.GetComponent<Transform>().childCount - 1; i >= 0; i--)
        {
            Transform child = transform.GetChild(i);
            child.gameObject.SetActive(false);
        }
        villagePlaces.SetActive(false);
    }


    
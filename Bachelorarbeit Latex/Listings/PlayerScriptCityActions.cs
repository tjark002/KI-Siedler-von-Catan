else if (plan.actions[i].GetType() == typeof(ActivateCityPlaces))
{
    gm.cityFocus.OnMouseDown();
    gm.Update(); //sicher gehen, dass Update mindestens einmal aufgerufen wurde.
}

else if (plan.actions[i].GetType() == typeof(Assets.Scripts.CBR.Plan.BuildCity))
{

    Assets.Scripts.CBR.Plan.BuildCity buildcity = (Assets.Scripts.CBR.Plan.BuildCity) plan.actions[i];
    if (gm.map.getCityPlaceByPosition(buildcity.row, buildcity.column).gameObject.activeSelf)
    {
        gm.map.getCityPlaceByPosition(buildcity.row, buildcity.column).gameObject.GetComponent<BuildCity>().Instantiate();
    }
}

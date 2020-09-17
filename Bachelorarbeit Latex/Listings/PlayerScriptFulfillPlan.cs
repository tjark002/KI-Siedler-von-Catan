public bool FulfillPlan(Plan plan)
{
    for (int i = 0; i < plan.GetActionCount(); i++)
    {
        if (plan.actions[i].GetType() == typeof(ActivateVillagePlaces))
        {
            gm.villageFocus.hasFocus = !gm.villageFocus.hasFocus;
            if (gm.villageFocus.hasFocus)
            {
                gm.roadFocus.hasFocus = false;
            }
            gm.Update(); //sicher gehen, dass Update mindestens einmal aufgerufen wurde.
        }
        else if (plan.actions[i].GetType() == typeof(ActivateRoadPlaces))
        {
            ...//Äquivalent zu ActivateVillagePlaces
        }
        else if (plan.actions[i].GetType() == typeof(BuildVillage))
        {
            //Zurzeit noch zufälliger Bauplatz
            Transform transform = gm.villagePlaces.GetComponent<Transform>();
            int rand = Random.Range(0, gm.villagePlaces.GetComponent<Transform>().childCount - 1);
            Transform child = transform.GetChild(rand);
            child.gameObject.GetComponent<buildVillage>().Instantiate();
        }
        else if (plan.actions[i].GetType() == typeof(Assets.Scripts.CBR.Plan.BuildRoad))
        {
            
            ... //Weitesgehend äquivalent zu BuildVillage
        }
        else if (plan.actions[i].GetType() == typeof(EndTurn))
        {
            if (gm.endTurnBtn.interactable)
                gm.OnEndTurn();
        }
        else if (plan.actions[i].GetType() == typeof(RollDice))
        {
            if (gm.rollDiceBtn.interactable)
                gm.OnRollDice();
        }
    }
    return true;
}
private void MakeAiTurn(float delay)
{
    StartCoroutine(ActivateAi(delay));
    StartCoroutine(ActivateAi(delay*2));
    StartCoroutine(ActivateAi(delay*3));
    StartCoroutine(ActivateAi(delay*4));
    StartCoroutine(ActivateAi(delay*5));
}


IEnumerator ActivateAi(float wait)
{
    yield return new WaitForSeconds(wait);
    Response response = SendToAI(endTurnBtn.interactable, rollDiceBtn.interactable);
    Plan plan = response.plan;
    plan.StringToActions();
    UnityEngine.Debug.Log("Plan " + plan.ToString());
    activePlayer.FulfillPlan(plan);
}

private void MakeAiMainTurn()
{
    StartCoroutine(ActivateAiMainTurn(4f));
}

IEnumerator ActivateAiMainTurn(float wait)
{
    yield return new WaitForSeconds(wait);
    Response response = SendToAI(endTurnBtn.interactable, rollDiceBtn.interactable);
    Plan plan = response.plan;
    plan.StringToActions();
    UnityEngine.Debug.Log("Plan " + plan.ToString());

    bool wantsToEndTurn = false;
    for (int i = 0; i < plan.actions.Count; i++) {
        if (plan.actions[i].GetType() == typeof(EndTurn))
        {
            wantsToEndTurn = true;
        }
    }
    activePlayer.FulfillPlan(plan);
    yield return new WaitForSeconds(wait);
    if (!wantsToEndTurn)
    {
        StartCoroutine(ActivateAiMainTurn(5f));
    }   
}
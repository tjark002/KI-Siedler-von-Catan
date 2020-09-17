for (int i = 0; i <= 3 &&  response.situation.player == null; i++)
{
    if (i < 3)
    {
        request = new Request(situation);
        response = connection.Send(request);
        UnityEngine.Debug.Log("Fehlversuch: " + i);
        Thread.Sleep(500);
    } else
    {
        activePlayer.FulfillPlan(new Plan());
    }
}
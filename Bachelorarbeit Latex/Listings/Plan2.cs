if (action.Contains("ActivateCityPlaces"))
{
    this.actions.Add(new ActivateCityPlaces());
}

if (action.Contains("BuildCity"))
{
    string[] splits = action.Split(':');
    this.actions.Add(new BuildCity(int.Parse(splits[1]), int.Parse(splits[2])));
}
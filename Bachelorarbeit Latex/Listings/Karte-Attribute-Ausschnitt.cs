
public enum Material
{
    brick,
    wheat,
    rock,
    wood,
    sheep,
    sand,
    ocean
}

[DataMember]
public List<Tile> tiles;


[DataMember]
public List<VillageBuildPlace> villageBuildPlaces;

[DataMember]
public List<RoadBuildPlace> roadBuildPlaces;
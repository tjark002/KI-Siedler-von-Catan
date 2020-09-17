public class VillageFocus : MonoBehaviour
{
    public  bool hasFocus = false;
    public RoadFocus roadFocus;

    private void OnMouseDown()
    {
        hasFocus = !hasFocus;
        if (hasFocus)
            roadFocus.hasFocus = false;
    }
}
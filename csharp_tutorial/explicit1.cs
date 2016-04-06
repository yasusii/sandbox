interface IDimensions
{
	float Length();
	float Width();
}

class Box: IDimensions
{
	float lengthinches;
	float widthinches;

	public Box(float length, float width)
	{
		lengthinches = length;
		widthinches = width;
	}

	float IDimensions.Length()
	{
		return lengthinches;
	}

	float IDimensions.Width()
	{
		return widthinches;
	}

	public static void Main()
	{
		Box myBox = new Box(30.0f, 20.0f);
		IDimensions myDimensions = (IDimensions)myBox;
		// System.Console.WriteLine("Length: {0}", myBox.Length());
		// System.Console.WriteLine("Length: {0}", myBox.Width());
		System.Console.WriteLine("Length: {0}", myDimensions.Length());
		System.Console.WriteLine("Length: {0}", myDimensions.Width());
	}
}

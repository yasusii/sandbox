interface IEnglishDimensions
{
	float Length();
	float Width();
}


interface IMetricDimensions
{
	float Length();
	float Width();
}


class Box: IEnglishDimensions, IMetricDimensions
{
	float lengthinches;
	float widthinches;

	public Box(float length, float width)
	{
		lengthinches = length;
		widthinches = width;
	}

	float IEnglishDimensions.Length()
	{
		return lengthinches;
	}

	float IEnglishDimensions.Width()
	{
		return widthinches;
	}

	float IMetricDimensions.Length()
	{
		return lengthinches * 2.54f;
	}

	float IMetricDimensions.Width()
	{
		return widthinches * 2.54f;
	}

	public static void Main()
	{
		Box myBox = new Box(30.0f, 20.0f);
		IEnglishDimensions eDimensions = (IEnglishDimensions)myBox;
		IMetricDimensions mDimensions = (IMetricDimensions)myBox;
		// System.Console.WriteLine("Length: {0}", myBox.Length());
		// System.Console.WriteLine("Length: {0}", myBox.Width());
		System.Console.WriteLine("Length(in): {0}", eDimensions.Length());
		System.Console.WriteLine("Length(in): {0}", eDimensions.Width());
		System.Console.WriteLine("Length(cm): {0}", mDimensions.Length());
		System.Console.WriteLine("Length(cm): {0}", mDimensions.Width());
	}
}

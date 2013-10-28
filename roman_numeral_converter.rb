class RomanNumeralConverter

	ROMAN_DIGITS = [ 
		["M", 1000],
		["CM", 900],
		["D", 500],
		["CD", 400],
		["C", 100],
		["XC", 90],
		["L", 50],
		["XL", 40],
		["XX", 20],
		["X", 10],
		["IX", 9],
		["V", 5],
		["IV", 4],
		["I", 1]
	]

	def convert(number)
		if number.is_a?(String) 
			convert_to_arabic(number)
		else
			convert_to_roman(number)
	  end
	end

	private

	def convert_to_arabic(number)
		sum = 0
		number.chars.each do |ch|
			sum += value_of(ch)
		end
		sum
	end

  def value_of(ch)
		if ch == "V"
			5
		elsif ch == "I"
			1
		end
	end

	def convert_to_roman(number)
		fail ArgumentError if number < 1
		result = ""
		ROMAN_DIGITS.each do |glyph, limit|
			while number >= limit
				result << glyph
				number -= limit
			end
		end
		result
	end
end

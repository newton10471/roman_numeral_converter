require 'rspec/given'
require './roman_numeral_converter'

RSpec::Given.use_natural_assertions

describe RomanNumeralConverter do
	Given(:converter) { RomanNumeralConverter.new }

	context "when converting from arabic to roman" do

		def as_roman(number)
			converter.convert(number)
		end

		Then { as_roman(1) == "I" }
		Then { as_roman(2) == "II" }
		Then { as_roman(4) == "IV" }
		Then { as_roman(5) == "V" }
		Then { as_roman(6) == "VI" }
		Then { as_roman(9) == "IX" }
		Then { as_roman(10) == "X" }
		Then { as_roman(20) == "XX" }
		Then { as_roman(40) == "XL" }
		Then { as_roman(50) == "L" }
		Then { as_roman(90) == "XC" }
		Then { as_roman(100) == "C" }
		Then { as_roman(400) == "CD" }
		Then { as_roman(500) == "D" }
		Then { as_roman(900) == "CM" }
		Then { as_roman(1000) == "M" }

		Then { as_roman(2013) == "MMXIII" }
		Then { as_roman(3999) == "MMMCMXCIX" }

		context "with an invalid number" do 
			When(:result) { as_roman(0) }
			Then { result.should have_failed(ArgumentError) }
		end
	end

	context "when converting from roman to arabic" do

		def as_arabic(number)
			converter.convert(number)
		end

		Then { as_arabic("I") == 1 }
		Then { as_arabic("II") == 2 }
		Then { as_arabic("IV") == 4 }
		Then { as_arabic("V") == 5 }
		Then { as_arabic("VI") == 6 }
		Then { pending; as_arabic("IX") == 9 }
		Then { pending; as_arabic("X") == 10 }
		Then { pending; as_arabic("XX") == 20 }
		Then { pending; as_arabic("XL") == 40 }
		Then { pending; as_arabic("L") == 50 }
		Then { pending; as_arabic("XC") == 90 }
		Then { pending; as_arabic("C") == 100 }
		Then { pending; as_arabic("CD") == 400 }
		Then { pending; as_arabic("D") == 500 }
		Then { pending; as_arabic("CM") == 900 }
		Then { pending; as_arabic("M") == 1000 }

		Then { pending; as_arabic("MMXIII") == 2013 }
		Then { pending; as_arabic("MMMCMXCIX") == 3999 }

		context "with an invalid number" do 
			When(:result) { as_arabic("") }
			Then { pending; result.should have_failed(ArgumentError) }
		end
	end
end

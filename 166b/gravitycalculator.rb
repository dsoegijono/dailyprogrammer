##
# http://www.reddit.com/r/dailyprogrammer/comments/284mep/6142014_challenge_166b_easy_planetary_gravity/
##

G = 6.67e-11

class Planet
  attr_reader :radius
  def initialize(r, d)
    @radius = r
    @density = d
    @volume = 4 * Math::PI * r**3 / 3
    @mass = @volume * d
  end
  
  def force(m)
    return G * m * @mass / @radius**2
  end
end

planets = {}
print "> "
m1 = gets.chomp.to_i
print "> "
n = gets.chomp.to_i

n.times do
  print "> "
  planet = gets.chomp.split(", ") #.map {|n| n.strip}
  planets[planet[0]] = Planet.new(planet[1].to_i, planet[2].to_i)
end

planets.each do |k, v|
  puts "#{k}: #{'%.3f' % v.force(m1)}"
end
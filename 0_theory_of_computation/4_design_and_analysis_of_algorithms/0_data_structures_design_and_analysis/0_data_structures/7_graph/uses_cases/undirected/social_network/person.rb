class Graph
    attr_accessor :network

    def initialize(people)
        @network = []
        @network = people
    end
end

class Person
    attr_accessor :name, :friends, :visited

    def initialize(name)
        @name = name
        @friends = []
        @visited = false
    end

    def add_friend(friend)
        @friends << friend
    end

    def display_network
        to_reset = [self]

        queue = [self]
        self.visited = true

        while queue.any?
            current_vertex = queue.shift
            puts current_vertex.name

            current_vertex.friends.each do |friend|
                if !friend.visited
                    to_reset << friend
                    queue << friend
                    friend.visited = true
                end
            end
        end

        to_reset.each do |node|
            node.visited =false
        end
    end
end

alice = Person.new("Alice")
bob = Person.new("Bob")
candy = Person.new("Candy")
thato = Person.new("Thato")
mpule = Person.new("Mpule")

alice.add_friend(bob)
alice.add_friend(candy)
alice.add_friend(thato)
alice.add_friend(mpule)

papudi = Person.new("Papudi")
kgobabala = Person.new("Kgobabala")
nape = Person.new("Nape")

bob.add_friend(papudi)
bob.add_friend(kgobabala)
bob.add_friend(nape)

shabi = Person.new("Shabi")
motlatsi = Person.new("Motlatsi")
thola = Person.new("Thola")

thato.add_friend(shabi)
thato.add_friend(motlatsi)
thato.add_friend(thola)

socialnetworkgrah = Graph.new([alice, bob, candy, thato, mpule, papudi, kgobabala, nape, shabi, motlatsi, thola])
#alice.display_network()
socialnetworkgrah.network[0].display_network()


'''
    Performance - display_network

        Time = 
            V = Number of nodes to process
            E = Number of edges

            O(V + 2E) = O(V + E)
                We process every node(V)
                We process every edge twice, starting from both connected nodes

        Space = 
            O(V)
                Storage for each node in the queue
'''

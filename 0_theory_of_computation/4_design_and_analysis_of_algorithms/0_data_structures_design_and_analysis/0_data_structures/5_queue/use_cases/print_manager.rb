class PrintManager
    def initialize
        @queue = []
    end

    def queue_print_job(document)
        @queue.push(document)
    end

    def run
        while @queue.any?
            print(@queue.shift)#removes and returns first element
        end
    end

    private def print(document)
        puts document
    end
end

print_manager = PrintManager.new
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")

print_manager.run


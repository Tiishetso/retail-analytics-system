export function Sidebar() {
  return (
    <div className="h-full p-4 flex flex-col">

      <h1 className="text-xl font-bold mb-6">
        WeatherIntel
      </h1>

      <nav className="flex flex-col gap-2">
        <button className="text-left px-3 py-2 rounded-lg hover:bg-muted">
          Overview
        </button>

        <button className="text-left px-3 py-2 rounded-lg hover:bg-muted">
          Weather
        </button>

        <button className="text-left px-3 py-2 rounded-lg hover:bg-muted">
          Market
        </button>

        <button className="text-left px-3 py-2 rounded-lg hover:bg-muted">
          Chatbot
        </button>
      </nav>

    </div>
  );
}
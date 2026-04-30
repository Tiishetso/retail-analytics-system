import { Sidebar } from "./Sidebar";
import { RightPanel } from "./RightPanel";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="h-screen w-full flex bg-muted/40">

      {/* Sidebar */}
      <div className="w-64 bg-background border-r">
        <Sidebar />
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">

        {/* Topbar */}
        <div className="h-16 border-b bg-background flex items-center px-6">
          <h1 className="font-semibold text-lg">Dashboard</h1>
        </div>

        {/* Page Content */}
        <div className="flex-1 p-6 overflow-y-auto">
          {children}
        </div>

      </div>

      {/* Right Panel */}
      <div className="w-80 bg-background border-l">
        <RightPanel />
      </div>

    </div>
  );
}
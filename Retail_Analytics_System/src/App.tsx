import DashboardLayout from "./components/ui/layout/DashboardLayout";
import { KpiCards } from "./components/ui/dashboard/KpiCards";
import { ChartsSection } from "./components/ui/dashboard/ChartsSection";

export default function App() {
  return (
    <DashboardLayout>
      <KpiCards />
      <ChartsSection />
    </DashboardLayout>
  );
}
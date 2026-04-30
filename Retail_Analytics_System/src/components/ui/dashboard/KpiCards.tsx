import { Card, CardContent } from "@/components/ui/card";

export function KpiCards() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

      <Card className="rounded-2xl shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-muted-foreground">
            Avg Temperature
          </p>
          <h2 className="text-2xl font-bold mt-2">
            28°C
          </h2>
        </CardContent>
      </Card>

      <Card className="rounded-2xl shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-muted-foreground">
            Economic Impact
          </p>
          <h2 className="text-2xl font-bold mt-2">
            -8%
          </h2>
        </CardContent>
      </Card>

      <Card className="rounded-2xl shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-muted-foreground">
            Risk Index
          </p>
          <h2 className="text-2xl font-bold mt-2">
            High
          </h2>
        </CardContent>
      </Card>

    </div>
  );
}
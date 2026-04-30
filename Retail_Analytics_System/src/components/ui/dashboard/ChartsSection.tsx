import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export function ChartsSection() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">

      {/* Weather Chart */}
      <Card className="rounded-2xl">
        <CardHeader>
          <CardTitle>Weather Trends</CardTitle>
        </CardHeader>
        <CardContent className="h-[300px] flex items-center justify-center text-muted-foreground">
          Chart coming soon
        </CardContent>
      </Card>

      {/* Economic Chart */}
      <Card className="rounded-2xl">
        <CardHeader>
          <CardTitle>Economic Impact</CardTitle>
        </CardHeader>
        <CardContent className="h-[300px] flex items-center justify-center text-muted-foreground">
          Chart coming soon
        </CardContent>
      </Card>

    </div>
  );
}
package mx.rmr.ppt.view
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import mx.rmr.ppt.ui.theme.PPTTheme

@Composable
fun AcercaDe(modifier: Modifier = Modifier) {
    Card(modifier = Modifier
        .fillMaxSize()
        .padding(16.dp)
        .border(
            1.dp,
            MaterialTheme.colorScheme.outline,
            shape = MaterialTheme.shapes.medium
        )
    ) {
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier.fillMaxSize()
        ) {
            Text(
                text = "Autor: Karen Abrego",
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth()
            )
        }
    }
}


@Preview(showBackground = true)
@Composable
fun AcercaDePreview(){
    PPTTheme {
        AcercaDe()
    }
}
